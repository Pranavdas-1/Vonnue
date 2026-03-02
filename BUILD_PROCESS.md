Day 1 (21/02/2026)

I initially contacted my friends Christo Jose and Jithu Girish to get a vague idea about the task whats the problem actually ment and what things to do and clarified my douts
From that conversation i got information about AKINATOR. I researched the algorithm in the youtube 

After researching with ChatGPT it gave me so me options they are
Weighted Scoring Model


Multi-Criteria Decision Analysis (MCDA)


Analytic Hierarchy Process (AHP) (optional advanced)


Rule-based scoring system
I tried to learn each of the techniques


# Speaker Decision Companion System  
## Final Clean Architectural Evolution Summary (Day 1 → Day 7)

---

## Phase 1 — Problem Framing (Day 1)

### What Happened
- Shared assignment mail with ChatGPT to understand expectations.
- Discussed with friends (Christo Jose, Jithu Girish).
- Learned about the Akinator-style decision logic.
- Researched Akinator algorithm on YouTube.

### Architectural State
- No architecture yet.
- Only conceptual understanding:
  - The system must guide a user to a decision.
  - It should behave like a structured decision engine.
  - It should not feel random.

### Key Insight
Decision-making systems must be:
- Structured
- Deterministic
- Explainable

---

## Phase 2 — Decision Model Exploration (Day 2–Day 3)

### Explored
- MCDA
- AHP
- Weighted Scoring
- Normalization
- TOPSIS
- Ambiguous problem solving

### Evolution of Thinking

| Stage | Thought |
|--------|--------|
| Early | Use AI to rank speakers |
| Mid | Use AHP |
| Later | Use MCDA |
| Final | Use deterministic mathematical TOPSIS |

### Why TOPSIS?
- Works well for numerical comparison.
- Clear separation of benefit vs cost.
- Mathematically explainable.
- Scalable to many criteria.

### Architectural Shift
Moved from:
> AI-based ranking

To:
> Deterministic multi-criteria mathematical scoring engine

---

## Phase 3 — Implementation Research (Day 4)

### Focus
- Web scraping feasibility
- Legal & ethical concerns
- BeautifulSoup
- Python venv setup
- Data availability from review websites

### Realization
Scraping introduces:
- Legal risks (Amazon, Flipkart)
- Inconsistent data
- Missing distortion/battery test details
- Blocked requests

### Architectural Decision
Do NOT rely fully on scraping.

Shift to:
- User input-driven system
- Structured input forms
- Optional advanced fields
- Deterministic engine independent of scraping

---

## Phase 4 — Deep Algorithm Engineering (Day 5)

### Major Work
- Compared AHP vs MCDA vs TOPSIS vs Fuzzy Logic
- Studied benefit vs cost attributes
- Learned normalization mathematically
- Built scoring pipeline:

1. Build matrix
2. Normalize
3. Apply weights
4. Identify ideal best/worst
5. Compute Euclidean distance
6. Rank

### Key Maturity
Understood:

- AHP is better for subjective hierarchy.
- MCDA is general framework.
- TOPSIS is computationally clean for numeric datasets.
- Fuzzy logic adds complexity and ambiguity.

### Architectural Outcome
Adopted:

> Structured TOPSIS + Penalty Engine

---

## Phase 5 — Application Structuring (Day 6)

### Major Evolution
Shift from:
> Algorithm prototype

To:
> Full web application architecture

### Introduced
- FastAPI backend
- Modular design:
  - decision_engine.py
  - explanation_engine.py
  - preprocessing.py
  - config.py
  - main.py

### Introduced User Segmentation

1. Casual Buyer
2. Audio Enthusiast
3. Technical Evaluator

### Why?
To reduce:
- Decision fatigue
- Cognitive overload
- Unnecessary advanced fields

### UX Architectural Insight
Different users need:
- Different levels of complexity.
- Different criteria exposure.
- Different explanation depth.

---

## Phase 6 — Criteria Refinement & Penalty Modeling

### Added

- Brand reliability penalty
- Clarity degradation penalty
- Battery honesty multiplier
- USB-C filter vs preference logic
- Direction-overridable attributes
- Separate weight adjustment page

### Mature Design Features

| Feature | Reason |
|----------|---------|
| Benefit / Cost override | Some users prefer heavier speakers |
| USB-C as filter | Not just weighted importance |
| Post-TOPSIS penalty multiplier | Maintain deterministic scoring |
| Explanation engine | Transparency |
| Weight separation page | UX clarity |

### Final Core Engine


User Input → Preprocess → Normalize → Apply Weights → TOPSIS →
Apply Penalty Multipliers → Rank → Generate Explanation


---

## Phase 7 — Architectural Simplification (Day 7)

### Realization
Three modes increased complexity unnecessarily.

### Decision
- Remove Enthusiast mode.
- Merge strong criteria into single refined system.
- Keep advanced criteria optional.

### Added Missing Criteria

- Mic
- Weight
- Price
- Bass scale
- Battery size (optional)
- Battery tested loudness (optional)
- Frequency range (advanced)
- Warranty
- App Support
- Number of Drivers
- Stand Orientation

### System Became

> A modular deterministic TOPSIS engine  
> with configurable penalties  
> with benefit/cost flexibility  
> with structured UI flow  

---

# Final Architecture

## 1️⃣ Backend

- FastAPI
- Modular structure
- No AI-based ranking
- Deterministic scoring

### Core Modules

- `decision_engine.py` → TOPSIS logic
- `preprocessing.py` → data cleaning & transformation
- `explanation_engine.py` → rule-based reasoning
- `config.py` → criteria & penalty configs
- `main.py` → routing & flow

---

## 2️⃣ Decision Logic

### Mathematical Steps

1. Construct decision matrix
2. Normalize columns
3. Multiply by weights
4. Identify ideal best & worst
5. Compute Euclidean distances
6. Compute closeness coefficient
7. Apply penalty multipliers
8. Sort descending

---

## 3️⃣ Penalty Architecture

Applied AFTER scoring:


Final Score = TOPSIS Score × BatteryHonesty × BrandFactor × DegradationFactor


This preserves mathematical clarity.

---

## 4️⃣ UX Flow

Landing Page  
→ Select User Type  
→ Enter Speakers  
→ Adjust Weights  
→ Apply Filters (USB-C etc.)  
→ View Ranked Results  
→ Explanation Breakdown  

---

## 5️⃣ Key Design Trade-offs

| Decision | Trade-off |
|----------|------------|
| Not using AI ranking | Lose adaptive learning, gain transparency |
| Not relying on scraping | Lose automation, gain stability |
| TOPSIS over AHP | Lose subjective hierarchy, gain scalability |
| Penalty multiplier instead of embedding inside matrix | Cleaner separation of concerns |
| Remove Enthusiast mode | Simpler architecture |

---

# Edge Cases Considered

- All speakers filtered out by USB-C
- Missing distortion data
- Missing battery test volume
- Non-monotonic attributes
- User overriding cost/benefit
- Less than 2 speakers
- Invalid numeric inputs

---

# Final Architectural Identity

The system evolved into:

> A deterministic, modular, penalty-aware, user-adaptive  
> multi-criteria decision support system  
> using structured TOPSIS scoring  
> built with FastAPI  
> optimized for explainability and extensibility.
---
---
---
BUILD_PROCESS.md

Project: Speaker Decision Companion System
Author: Pranav Das
Core Model: Deterministic TOPSIS-based MCDA

1. How I Started

The assignment required building a Decision Companion System that:

Accepts multiple options

Accepts multiple criteria with different importance

Produces a ranked output

Explains why a decision was made

Does not rely entirely on AI

I initially approached this as a classical Multi-Criteria Decision Analysis (MCDA) problem.

After evaluating options like:

Weighted Scoring Model

AHP (Analytic Hierarchy Process)

TOPSIS

I selected TOPSIS because:

It naturally handles both benefit and cost criteria

It ranks alternatives based on distance from ideal best/worst

It is mathematically deterministic

It is explainable (no black-box behavior)

It scales well with multiple speakers

2. Initial Architecture Plan

The first architectural design separated:

Decision Engine (TOPSIS)

Explanation Engine

Preprocessing Layer

FastAPI Web Layer

This separation ensured:

No business logic inside routes

Deterministic scoring

Clean modular structure

Easy refactoring

The TOPSIS engine was intentionally kept framework-independent.

3. Early Feature Expansion (Over-Engineering Phase)

Initially, I introduced:

Multiple user modes (Casual / Enthusiast)

Advanced penalty stacking

Brand reliability multipliers

Battery honesty penalty controls

Clarity degradation factors

Although these features were technically interesting, I later realized:

They increased cognitive load

They expanded scope beyond assignment requirements

They reduced clarity of the core system

This phase helped me understand trade-offs between feature richness and architectural clarity.

4. Refactoring & Scope Reduction

After review, I simplified the system to focus on:

One primary mode (Casual Buyer)

Strong but meaningful criteria

Clear cost/benefit categorization

Explicit weight normalization

Controlled constraint modeling (USB-C logic)

I removed:

Enthusiast mode routes

Advanced penalty stacking

Overlapping configuration layers

Redundant complexity

This reduced system complexity while preserving modeling depth.

5. Criteria Design Evolution
Phase 1 — Technical Specs

Initially focused heavily on raw technical specs:

Bluetooth version

Frequency response

Driver size

Codec types

This proved unsuitable for general users.

Phase 2 — Outcome-Based Criteria

I restructured criteria into:

Sound Clarity

Bass Strength

Loudness

Battery Life

Portability

Build Quality

IP Rating

Price

Physical Weight

Brand Reliability

App Support

Warranty

Stand Orientation

This balanced usability with technical depth.

6. Cost vs Benefit Classification

A critical realization:

TOPSIS requires explicit categorization of criteria:

Benefit → higher is better

Cost → lower is better

Final classification:

Cost Criteria:

Price

Physical Weight

Benefit Criteria:

All others

Additionally, selected criteria allow direction override (user-controlled benefit/cost).

7. Charging Type Modeling Decision

Charging Type (USB-C) was not treated as a normal weighted criterion.

Instead:

"Must Be USB-C" → Pre-TOPSIS filtering

"Prefer USB-C" → Post-score penalty

"Don’t Care" → Ignored

This separates:

Constraint logic

Preference logic

Performance scoring

This improved mathematical integrity.

8. Weight Normalization

Users assign importance on a 1–5 scale.

Before feeding into TOPSIS:

𝑤
𝑖
=
𝑤
𝑖
∑
𝑤
w
i
	​

=
∑w
w
i
	​

	​


This ensures:

Proper normalization

No artificial bias

Stable ranking behavior

9. Explanation Engine

The explanation engine:

Identifies top contributing criteria

Highlights weaknesses

Reports applied penalties

Produces deterministic textual reasoning

No generative AI is used for explanation.
All explanations are derived from computed metrics.

10. Mistakes & Corrections
Mistake 1 — Over-Expanding Modes

Initially introduced multiple user personas.
Correction: Reduced to a focused, clear system.

Mistake 2 — Penalty Stacking Complexity

Advanced multipliers added complexity without proportional value.
Correction: Simplified to core, explainable logic.

Mistake 3 — Treating All Criteria Equally

Charging type was initially weighted like other criteria.
Correction: Modeled it as constraint + soft penalty instead.

11. Final Architecture
FastAPI Routes
      ↓
Preprocessing Layer
      ↓
TOPSIS Decision Engine
      ↓
Explanation Engine
      ↓
Result Rendering

Key Principles:

Deterministic logic

Transparent scoring

Modular separation

Minimal scope creep

Clear mathematical foundation

12. What I Would Improve With More Time

If extended further:

Add persistent session handling instead of in-memory dict

Add visual explanation graphs

Add scenario presets (Battery-focused / Party-focused)

Add structured product dataset ingestion

Add confidence modeling for missing data

13. Final Reflection

The biggest learning was not about implementing TOPSIS.
