# Vonnue — Speaker Decision Companion

This is a deterministic web-based Decision Companion System for ranking Bluetooth / portable speakers using the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) multi-criteria decision algorithm.

The system compares multiple speakers across structured, weighted criteria and produces an objective, explainable ranking.

Live Demo:  
https://vonnue.onrender.com/

---

## 1. Understanding of the Problem

Buying a speaker involves evaluating multiple competing criteria:

- Price vs Performance  
- Battery Life vs Loudness  
- Portability vs Durability  
- Feature Set vs Build Quality  

Most decisions are made subjectively through reviews, marketing claims, or informal comparisons.

The goal of this system is to:

- Accept multiple speaker options  
- Accept multiple criteria with varying importance  
- Process both benefit and cost attributes  
- Produce a ranked recommendation  
- Clearly explain why a speaker ranks higher  

The system must be deterministic, transparent, and not rely entirely on AI models.

---

## 2. Solution Approach

The system uses TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution), a classical Multi-Criteria Decision Analysis (MCDA) method.

Each speaker is modeled as a vector across multiple dimensions.

Evaluation steps:

1. Construct decision matrix  
2. Normalize matrix (vector normalization)  
3. Apply user-defined weights  
4. Compute ideal best and ideal worst solutions  
5. Calculate Euclidean distance from both  
6. Compute closeness coefficient  

Final score:

Cᵢ = D⁻ / (D⁺ + D⁻)

Where:
- D⁺ = distance from ideal best  
- D⁻ = distance from ideal worst  

Speakers closer to the ideal best receive higher scores.

No generative AI is used in ranking.

---

## 3. Criteria Structure

The system evaluates speakers across 18 criteria, including:

- Price (Cost)
- Physical Weight (Cost)
- Sound Clarity
- Bass Strength
- Output Power (Wattage)
- Battery Life
- Battery Size (optional)
- IP Rating
- Bluetooth Version
- Number of Drivers
- Warranty (Years)
- Brand Reliability
- App Support
- Stand Orientation
- Microphone Support
- Charging Wattage
- Multi-Pairing Support
- USB-C Preference Logic

Users assign importance (1–5 scale) to each criterion.  
Weights are normalized before evaluation.

Selected criteria (e.g., Price, Weight) allow direction override (Higher is Better / Lower is Better).

---

## 4. Assumptions Made

- All numeric inputs are valid and comparable across speakers.
- User-entered data is trusted (no automated scraping used).
- Brand reliability is user-defined, not externally validated.
- Missing optional fields are treated neutrally.
- USB-C preference is modeled as constraint or penalty rather than weighted attribute.

---

## 5. Design Decisions and Trade-offs

### Deterministic Model over AI
Although AI could estimate product attributes, the ranking engine is fully deterministic to ensure explainability and reproducibility.

### Separation of Layers
Architecture separates:

- Preprocessing Layer  
- Decision Engine (TOPSIS)  
- Explanation Engine  
- Web Interface  

This ensures modularity and testability.

### Charging Type Modeling
Charging type is treated as:
- Hard constraint (filter)
- Soft penalty  
Instead of a weighted criterion to avoid distorting normalization.

### Reduced Mode Complexity
An earlier version included multiple user modes (Casual / Enthusiast).  
This was simplified to maintain clarity and avoid scope creep.

---

## 6. Edge Cases Considered

- Less than two speakers submitted
- All speakers filtered due to USB-C constraint
- Zero total weight (fallback normalization)
- Optional fields missing (battery size, etc.)
- Direction override conflicts
- Invalid numeric conversions
- Speakers tied in score

---

## 7. Project Structure

```
Vonnue.1/
├── app/
│   ├── config.py
│   ├── decision_engine.py
│   ├── explanation_engine.py
│   ├── preprocessing.py
│   ├── main.py
│   ├── static/
│   └── templates/
└── requirements.txt
```

---

## 8. Tech Stack

Backend: FastAPI  
Server: Uvicorn  
Algorithm: TOPSIS (NumPy)  
Templating: Jinja2  
Frontend: HTML / CSS / Vanilla JS  
Hosting: Render  

---

## 9. How to Run

Clone:

```
git clone https://github.com/Pranavdas-1/Vonnue.1
cd Vonnue.1
pip install -r requirements.txt
```

Run:

```
python -m uvicorn app.main:app --reload --port 8000
```

Open:

```
http://127.0.0.1:8000
```

Live Deployment:

https://vonnue.onrender.com/

---

## 10. Repository Notes

The original development repository with early commit history was deleted during restructuring.

Current repositories:

Main Application:  
https://github.com/Pranavdas-1/Vonnue.1  

Standalone TOPSIS Development (algorithm experimentation):  
https://github.com/Pranavdas-1/Topsis_algorithm  

The current repository reflects the finalized structured implementation.

---

## 11. What I Would Improve With More Time

- Replace in-memory session storage with persistent session management
- Add structured product dataset import
- Add visual decision contribution graphs
- Implement preset decision profiles (Battery-focused, Party-focused, etc.)
- Add confidence modeling for missing attributes
- Improve commit history clarity (earlier repository deletion reduced traceability)

---

## 12. Final Reflection

This project emphasizes:

- Structured problem modeling
- Clear separation of concerns
- Deterministic ranking logic
- Explainable outputs
- Controlled scope management

The system demonstrates practical application of MCDA in real-world consumer decision support.
