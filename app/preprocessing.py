"""
preprocessing.py — Form data preprocessing for Casual Buyer mode.

Converts raw UI form data into Speaker and Criterion objects
compatible with the TOPSIS decision engine.
"""

import re
from typing import Dict, List, Tuple

from app.decision_engine import Criterion, Speaker
from app.config import (
    CRITERIA_KEYS, CRITERIA_TYPES, DIRECTION_OVERRIDABLE,
    APP_SUPPORT_MAP, BRAND_RELIABILITY_MAP, STAND_ORIENTATION_MAP,
)


# ───────────────────────────────────────────────────
#  Dropdown value maps
# ───────────────────────────────────────────────────

CLARITY_MAP = {
    "Bad": 1, "Average": 2, "Good": 3, "Very Good": 4, "Excellent": 5,
}

CHARGING_TYPE_MAP = {
    "Micro-USB": 1, "USB-C": 3, "Type-C Fast Charging": 5,
}

BUILD_QUALITY_MAP = {
    "Poor": 1, "Average": 2, "Good": 3, "Premium": 5,
}

MULTI_PAIRING_MAP = {
    "No": 0, "Yes (Stereo)": 3, "Yes (Party Mode)": 5,
}

MIC_MAP = {
    "No": 0, "Yes": 5,
}


# ───────────────────────────────────────────────────
#  Conversion helpers
# ───────────────────────────────────────────────────

def map_clarity(value: str) -> float:
    return float(CLARITY_MAP.get(value, 1))

def map_build(value: str) -> float:
    return float(BUILD_QUALITY_MAP.get(value, 1))

def map_multi_pair(value: str) -> float:
    return float(MULTI_PAIRING_MAP.get(value, 0))

def map_mic(value: str) -> float:
    return float(MIC_MAP.get(value, 0))

def map_app_support(value: str) -> float:
    return float(APP_SUPPORT_MAP.get(value, 0))

def map_brand_reliability(value: str) -> float:
    return float(BRAND_RELIABILITY_MAP.get(value, 1))

def map_stand_orientation(value: str) -> float:
    return float(STAND_ORIENTATION_MAP.get(value, 1))

def extract_ip_value(ip_string: str) -> float:
    numbers = re.findall(r'\d+', ip_string)
    if not numbers:
        return 0.0
    return float(numbers[-1])


# Map of criterion key → converter function
_CONVERTERS: Dict[str, callable] = {
    "clarity": map_clarity,
    "build": map_build,
    "multi_pair": map_multi_pair,
    "mic": map_mic,
    "ip": extract_ip_value,
    "app_support": map_app_support,
    "brand_reliability": map_brand_reliability,
    "stand_orientation": map_stand_orientation,
}


def _parse_value(key: str, raw: str) -> float:
    """Convert a raw form string to a numeric value."""
    if key in _CONVERTERS:
        return _CONVERTERS[key](raw)
    return float(raw) if raw else 0.0


# ───────────────────────────────────────────────────
#  Weight normalisation
# ───────────────────────────────────────────────────

def normalize_weights(weight_dict: Dict[str, int]) -> Dict[str, float]:
    total = sum(weight_dict.values())
    if total == 0:
        return {k: 1 / len(weight_dict) for k in weight_dict}
    return {k: v / total for k, v in weight_dict.items()}


# ───────────────────────────────────────────────────
#  Main preprocessing function
# ───────────────────────────────────────────────────

def preprocess_speakers(
    form_data: Dict[str, str],
    weight_inputs: Dict[str, int],
    direction_inputs: Dict[str, str] | None = None,
) -> Tuple[List[Speaker], List[Criterion]]:
    """Convert raw form data + weight inputs into Speaker and Criterion lists."""
    normalized = normalize_weights(weight_inputs)

    if direction_inputs is None:
        direction_inputs = {}

    criteria = [
        Criterion(
            key,
            normalized[key],
            direction_inputs.get(key, CRITERIA_TYPES[key]),
        )
        for key in CRITERIA_KEYS
    ]

    speakers: List[Speaker] = []
    speaker_count = int(form_data["speaker_count"])

    for i in range(speaker_count):
        attributes: Dict[str, float] = {}
        for key in CRITERIA_KEYS:
            raw = form_data.get(f"{key}_{i}", "").strip()
            attributes[key] = _parse_value(key, raw)

        raw_charging = form_data.get(f"charging_type_{i}", "Micro-USB")

        speaker = Speaker(
            name=form_data[f"name_{i}"],
            attributes=attributes,
            battery_test_volume=80.0,
        )
        speaker._charging_type_raw = raw_charging
        speakers.append(speaker)

    return speakers, criteria
