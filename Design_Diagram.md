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

- X = Decision Matrix  
- w = Weight Vector  
- v = Weighted Normalized Matrix  

---

### Step 1 — Normalize

Vector normalization is applied column-wise:

r_ij = x_ij / sqrt( Σ (x_ij²) )

Where:
- r_ij = normalized value  
- x_ij = original value  
- Denominator = square root of sum of squares of that column  

---

### Step 2 — Apply Weights

v_ij = w_j × r_ij

Each normalized column is multiplied by its corresponding weight.

---

### Step 3 — Identify Ideal Solutions

For Benefit Criteria (higher is better):

A⁺ = max(v_ij)  
A⁻ = min(v_ij)

For Cost Criteria (lower is better):

A⁺ = min(v_ij)  
A⁻ = max(v_ij)

A⁺ = Ideal Best  
A⁻ = Ideal Worst  

---

### Step 4 — Compute Distances

Distance from Ideal Best:

D_i⁺ = sqrt( Σ (v_ij − A⁺)² )

Distance from Ideal Worst:

D_i⁻ = sqrt( Σ (v_ij − A⁻)² )

---

### Step 5 — Closeness Coefficient

C_i = D_i⁻ / (D_i⁺ + D_i⁻)

Where:

- Higher C_i means closer to ideal best  
- 0 ≤ C_i ≤ 1  

---

### Step 6 — Apply Penalty Model

FinalScore = C_i × BatteryFactor × BrandFactor × DegradationFactor

Penalty multipliers are applied **after** TOPSIS scoring to preserve matrix integrity.

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
