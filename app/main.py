"""
main.py — FastAPI application entry point.

Single mode: Casual Buyer.
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import (
    CRITERIA_KEYS, CRITERIA_TYPES, CRITERIA_LABELS,
    DIRECTION_OVERRIDABLE,
)
from app.decision_engine import TOPSISDecisionEngine
from app.explanation_engine import generate_explanation
from app.preprocessing import (
    preprocess_speakers,
    CLARITY_MAP, CHARGING_TYPE_MAP, BUILD_QUALITY_MAP,
    MULTI_PAIRING_MAP, MIC_MAP,
)

# ------------------------------------------------------------------ #
#  App initialisation
# ------------------------------------------------------------------ #

app = FastAPI(
    title="Speaker Decision Companion",
    description="Deterministic speaker ranking system using TOPSIS.",
    version="0.4.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# ------------------------------------------------------------------ #
#  In-memory session state
# ------------------------------------------------------------------ #

_session: dict = {}

# ------------------------------------------------------------------ #
#  Routes
# ------------------------------------------------------------------ #


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return RedirectResponse(url="/casual/speakers", status_code=303)


@app.get("/casual/speakers", response_class=HTMLResponse)
async def casual_speakers_form(request: Request):
    return templates.TemplateResponse(
        "casual_speakers.html",
        {
            "request": request, "title": "Enter Speaker Details",
            "clarity_options": list(CLARITY_MAP.keys()),
            "charging_type_options": list(CHARGING_TYPE_MAP.keys()),
            "build_options": list(BUILD_QUALITY_MAP.keys()),
            "multi_pair_options": list(MULTI_PAIRING_MAP.keys()),
            "mic_options": list(MIC_MAP.keys()),
            "active_step": "speakers",
        },
    )


@app.post("/casual/speakers")
async def casual_speakers_submit(request: Request):
    form = await request.form()
    _session["speaker_form"] = dict(form)
    return RedirectResponse(url="/casual/weights", status_code=303)


@app.get("/casual/weights", response_class=HTMLResponse)
async def casual_weights_form(request: Request):
    if "speaker_form" not in _session:
        return RedirectResponse(url="/casual/speakers", status_code=303)
    return templates.TemplateResponse(
        "casual_weights.html",
        {
            "request": request, "title": "Adjust Criteria Importance",
            "criteria_keys": CRITERIA_KEYS,
            "criteria_labels": CRITERIA_LABELS,
            "criteria_types": CRITERIA_TYPES,
            "direction_overridable": DIRECTION_OVERRIDABLE,
            "active_step": "weights",
        },
    )


@app.post("/casual/weights")
async def casual_weights_submit(request: Request):
    if "speaker_form" not in _session:
        return RedirectResponse(url="/casual/speakers", status_code=303)

    form = await request.form()
    weight_inputs = {key: int(form.get(f"weight_{key}", 3)) for key in CRITERIA_KEYS}

    direction_inputs = {}
    for key in DIRECTION_OVERRIDABLE:
        raw = form.get(f"direction_{key}", "").strip()
        if raw in ("benefit", "cost"):
            direction_inputs[key] = raw

    charging_pref = form.get("charging_pref", "dont_care").strip()
    speakers, criteria = preprocess_speakers(
        _session["speaker_form"], weight_inputs, direction_inputs
    )

    # Charging filter/penalty
    filtered_out = []
    if charging_pref == "must_usbc":
        kept = []
        for s in speakers:
            raw_ct = getattr(s, "_charging_type_raw", "")
            if "USB-C" in raw_ct or "Type-C" in raw_ct:
                kept.append(s)
            else:
                filtered_out.append(s.name)
        speakers = kept

    if len(speakers) < 2:
        _session["filter_error"] = "All speakers filtered out by Must Be USB-C."
        return RedirectResponse(url="/casual/weights", status_code=303)

    engine = TOPSISDecisionEngine(criteria)
    ranking, weighted_matrix, ideal_best = engine.evaluate(speakers)

    results = []
    for speaker, score in ranking:
        idx = speakers.index(speaker)
        adjusted = float(score)
        notes = []
        if charging_pref == "prefer_usbc":
            raw_ct = getattr(speaker, "_charging_type_raw", "")
            if "USB-C" not in raw_ct and "Type-C" not in raw_ct:
                adjusted *= 0.85
                notes.append("Non-USB-C penalty (×0.85).")

        explanation = generate_explanation(speaker, score, weighted_matrix[idx], criteria, ideal_best)
        if notes:
            explanation += " " + " ".join(notes)
        results.append({"name": speaker.name, "score": round(adjusted, 4),
                         "explanation": explanation, "rank": 0})

    results.sort(key=lambda r: r["score"], reverse=True)
    for i, r in enumerate(results):
        r["rank"] = i + 1
    if filtered_out:
        results.append({"name": ", ".join(filtered_out), "score": None,
                         "explanation": "Filtered out — does not use USB-C.", "rank": None})

    _session["results"] = results
    return RedirectResponse(url="/casual/results", status_code=303)


@app.get("/casual/results", response_class=HTMLResponse)
async def casual_results(request: Request):
    results = _session.get("results")
    if not results:
        return RedirectResponse(url="/casual/speakers", status_code=303)
    return templates.TemplateResponse(
        "casual_results.html",
        {"request": request, "title": "Ranking Results",
         "results": results, "active_step": "results"},
    )
