# 1. Architecture Diagram

## High-Level System Architecture

```
                ┌──────────────────────────┐
                │        User Browser       │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │      FastAPI Router      │
                │        (main.py)         │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     Preprocessing Layer  │
                │     (preprocessing.py)   │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Decision Engine        │
                │   (decision_engine.py)   │
                │        TOPSIS            │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Penalty Multipliers    │
                │ (Brand / Battery / etc.) │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │  Explanation Engine      │
                │ (explanation_engine.py)  │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   HTML Template Render   │
                └──────────────────────────┘
```

### Architectural Characteristics

- Deterministic scoring
- Clear separation of concerns
- No business logic inside routes
- Framework-independent scoring engine
- Penalty modeling isolated from TOPSIS core

---

# 2. Data Flow Diagram

## End-to-End Data Flow

```
User Inputs Speaker Data
        │
        ▼
Form Submission
        │
        ▼
Data Type Conversion
(String → Float → Scale Mapping)
        │
        ▼
Decision Matrix Construction
        │
        ▼
Normalization (Vector Normalization)
        │
        ▼
Weight Application
        │
        ▼
Ideal Best & Worst Identification
        │
        ▼
Distance Calculation (Euclidean)
        │
        ▼
Closeness Coefficient Computation
        │
        ▼
Apply Penalty Multipliers
        │
        ▼
Sort Speakers by Final Score
        │
        ▼
Generate Deterministic Explanation
        │
        ▼
Render Results Page
```

---

# 3. Decision Logic Diagram

## Mathematical Flow (TOPSIS)

Let:

- \( X \) = Decision Matrix  
- \( w \) = Weight Vector  
- \( v \) = Weighted Normalized Matrix  

---

### Step 1 — Normalize

\[
r_{ij} = \frac{x_{ij}}{\sqrt{\sum x_{ij}^2}}
\]

---

### Step 2 — Apply Weights

\[
v_{ij} = w_j \cdot r_{ij}
\]

---

### Step 3 — Identify Ideal Solutions

For Benefit Criteria:

\[
A^+ = \max(v_{ij})
\]

\[
A^- = \min(v_{ij})
\]

For Cost Criteria:

\[
A^+ = \min(v_{ij})
\]

\[
A^- = \max(v_{ij})
\]

---

### Step 4 — Compute Distances

\[
D_i^+ = \sqrt{\sum (v_{ij} - A^+)^2}
\]

\[
D_i^- = \sqrt{\sum (v_{ij} - A^-)^2}
\]

---

### Step 5 — Closeness Coefficient

\[
C_i = \frac{D_i^-}{D_i^+ + D_i^-}
\]

---

### Step 6 — Apply Penalty Model

\[
FinalScore = C_i \times BatteryFactor \times BrandFactor \times DegradationFactor
\]

---

# 4. Component Diagram

```
app/
│
├── main.py
│     └── Handles HTTP routes & flow
│
├── decision_engine.py
│     └── Pure TOPSIS logic
│
├── preprocessing.py
│     └── Converts form data → structured matrix
│
├── explanation_engine.py
│     └── Generates rule-based reasoning
│
├── config.py
│     └── Criteria definitions & penalty values
│
└── templates/
      └── HTML rendering layer
```

---

# 5. Design Principles

1. Deterministic decision logic  
2. Transparent scoring  
3. Modular architecture  
4. Clear separation of concerns  
5. Constraint vs preference modeling  
6. No AI-based ranking  
7. Extensible criteria configuration  

---

# 6. Why This Design?

- TOPSIS ensures mathematical consistency.
- Penalties applied post-scoring preserve matrix integrity.
- Charging logic separated to prevent distortion of weights.
- Explanation engine increases interpretability.
- Modular backend enables future extension (e.g., alternate MCDA models).

---

# 7. System Identity

The system is a:

Deterministic, modular, penalty-aware, multi-criteria decision support application built using FastAPI and structured TOPSIS scoring.

It is designed for:

- Explainability  
- Extensibility  
- Stability  
- Mathematical transparency  

No AI model is used in ranking decisions.
