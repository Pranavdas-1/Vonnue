# BUILD_PROCESS.md

## Speaker Decision Companion System  
### Development Evolution Log (Day 1 → Day 7)

---

# Day 1 — 21/02/2026  
## Phase 1 — Problem Framing

### How I Started

The assignment was intentionally ambiguous.  
It did not ask for a specific algorithm, technology, or domain.

It emphasized:

- Clarity of thinking  
- System design maturity  
- Transparency  
- Decision reasoning  

To better understand the expectations, I:

- Shared the assignment mail with ChatGPT.
- Discussed the problem with Christo Jose and Jithu Girish.
- Clarified what “Decision Companion System” truly meant.
- Explored how structured decision systems work.

During this discussion, I was introduced to the concept of **Akinator-style logic** — a system that narrows decisions through structured questioning.

I researched the Akinator algorithm on YouTube to understand:

- How it structures knowledge.
- How it narrows decision space.
- How it avoids randomness.

---

### Personal Context That Influenced the Idea

At the same time, I had been researching Bluetooth speakers for my car for almost 5–6 days.

As a buyer, I had already explored:

- Battery life
- Clarity
- Distortion
- Bass quality
- IP rating
- Charging type
- Brand reliability
- Multi-pairing
- Long-term degradation

I noticed:

- Most decisions were based on subjective reviews.
- Specifications were scattered.
- Marketing claims were misleading (e.g., battery life tested at 50–60% volume).
- There was no structured way to compare speakers objectively.

This real-world frustration directly influenced the domain selection.

I did not want to build a generic decision system.  
I wanted to build one I would personally use.

This allowed me to think both:

- As a developer (architectural clarity)
- As a user (decision pain points)

---

### Early Algorithm Exploration

After discussing with ChatGPT, I explored multiple possible approaches:

- Weighted Scoring Model
- Multi-Criteria Decision Analysis (MCDA)
- Analytic Hierarchy Process (AHP) (optional advanced)
- Rule-based scoring system

I studied each technique at a high level.

At this stage, no implementation existed.  
Only conceptual understanding.

---

### Architectural State (End of Day 1)

No formal architecture.

Only guiding principles:

- The system must guide a user to a decision.
- It must not behave randomly.
- It must not be a hardcoded comparison.
- It must produce explainable output.
- It must feel structured and rational.

---

### Alternative Approaches Considered

1. Pure Akinator-style question tree  
   Rejected because:
   - Not scalable for numeric comparisons.
   - Hard to extend with many attributes.

2. Simple rule-based if-else logic  
   Rejected because:
   - Becomes messy with 15–20 criteria.
   - Hard to justify mathematically.

3. AI-driven ranking  
   Rejected immediately because:
   - Assignment required deterministic explainability.
   - Black-box models would violate constraints.

---

### Key Insight From Day 1

A decision system must be:

- Structured  
- Deterministic  
- Explainable  
- User-controllable  

And most importantly:

It must transform ambiguity into measurable comparison.

---

### What Changed in My Thinking

Before Day 1:
- I was thinking in terms of building "something functional."

After Day 1:
- I started thinking in terms of building a **decision architecture**.

This shift from coding-first to thinking-first defined the rest of the project.

---

### Mistakes / Early Misconceptions

- Initially thought Akinator-style questioning might be sufficient.
- Underestimated the complexity of multi-criteria comparison.
- Considered using AI more heavily before fully understanding assignment constraints.

These misconceptions were corrected through structured research and discussion.

---

### Foundation Established

Day 1 did not produce code.

It produced:

- Direction
- Constraints
- Architectural philosophy
- Domain clarity (Bluetooth speaker decision system)

This became the foundation for everything built afterward.

# Phase 2 — Decision Model Exploration (Day 2–Day 3)

## Context

After Day 1 clarified that the system must be structured, deterministic, and explainable,  
the next challenge was:

**What decision model should power the system?**

At this stage, the system had:

- A domain (Bluetooth speakers)
- Clear user pain points
- No mathematical backbone

Day 2 and Day 3 were focused entirely on solving that.

---

## What I Explored

- MCDA (Multi-Criteria Decision Analysis)
- AHP (Analytic Hierarchy Process)
- Weighted Scoring Model
- Rule-based systems
- Normalization techniques
- TOPSIS
- Fuzzy logic
- Ambiguous problem structuring

I did not immediately jump into implementation.

I first tried to understand:

- Which model fits structured product comparison?
- Which model scales?
- Which model remains explainable?
- Which model avoids black-box behavior?

---

## Evolution of Thinking

| Stage | Thought Process |
|--------|----------------|
| Early | Use AI to rank speakers dynamically |
| Realization | AI ranking violates determinism & explainability |
| Mid | Use AHP because it is "advanced" |
| Concern | AHP becomes complex with many criteria |
| Later | Use MCDA weighted scoring |
| Refined | Use normalized weighted scoring |
| Final | Adopt TOPSIS for mathematically structured ranking |

---

## Initial Mistake — AI-Based Ranking

Initially, I considered:

> “Why not use AI to evaluate speakers?”

This was rejected because:

- It becomes a black-box.
- Hard to justify mathematically.
- Violates assignment requirement of explainability.
- Cannot transparently show why one speaker ranks higher.

This was the first major architectural correction.

---

## AHP Exploration

I studied:

- Pairwise comparison matrix
- Consistency ratio
- Eigenvector-based weight extraction

Why it looked attractive:
- Theoretically rigorous.
- Academic and structured.

Why I moved away:
- Becomes computationally heavy with many criteria.
- Requires too many pairwise comparisons.
- Poor scalability if criteria > 8–10.
- Not necessary when data is mostly numeric.

However, I did not discard it blindly.  
I considered conditional logic:

> If criteria ≤ 8 → AHP  
> If criteria > 8 → MCDA/TOPSIS  

This showed progression from blind adoption to contextual thinking.

---

## MCDA & Weighted Scoring Phase

I then explored classical weighted scoring:

Final Score = Σ (weight × normalized value)

Advantages:
- Simple.
- Scalable.
- Easy to explain.

Limitations discovered:
- No ideal-best vs ideal-worst reference.
- Ranking sensitivity when values cluster closely.
- No structural separation of benefit and cost extremes.

This led to deeper research.

---

## Why TOPSIS Emerged

Through comparison, TOPSIS provided:

- Vector normalization.
- Clear benefit vs cost classification.
- Ideal best solution.
- Ideal worst solution.
- Euclidean distance calculation.
- Closeness coefficient ranking.

Mathematically:

Ci = D⁻ / (D⁺ + D⁻)

Where:
- D⁺ = Distance from ideal best
- D⁻ = Distance from ideal worst

Why this was powerful:

- Not just weighted sum.
- Measures relative closeness to perfection.
- Works naturally for numeric datasets.
- Scales with many criteria.
- Completely deterministic.
- Fully explainable step-by-step.

This matched all Day 1 constraints.

---

## Architectural Shift

Moved from:

> AI-based ranking

To:

> Deterministic multi-criteria mathematical scoring engine

And refined further to:

> Modular TOPSIS engine with configurable penalties

---

## Penalty Modeling Evolution

While studying TOPSIS, I identified real-world issues:

- Battery tested at 50–60% volume.
- Brand clarity degradation after 6–8 months.
- Misleading wattage claims.
- Micro-USB vs USB-C differences.

This triggered the idea:

> The model should not blindly trust raw specifications.

So I integrated:

- Penalty multipliers.
- Post-score adjustments.
- Reliability modeling.

This added realism without sacrificing determinism.

---

## Code-Level Deep Dive

At this stage, I did not blindly use library code.

I asked detailed questions about:

- Matrix construction
- Normalization math
- Ideal solution computation
- Euclidean distance formula
- Benefit vs cost categorization
- Distance vector interpretation

This was intentional.

I wanted to:

- Fully understand the math.
- Avoid treating TOPSIS as a black box.
- Ensure I can explain every step during evaluation.

---

## Mistakes and Corrections

1. Initially overestimated AHP suitability.
2. Considered fuzzy logic unnecessarily.
3. Thought complexity equals sophistication.
4. Underestimated decision fatigue caused by too many criteria.

Corrections:

- Simplified model.
- Reduced unnecessary abstraction.
- Focused on numeric structured comparison.
- Chose clarity over algorithmic complexity.

---

## What Changed in My Thinking

Before Phase 2:
- I was choosing an algorithm.

After Phase 2:
- I was designing a decision engine.

Shifted focus from:

> “Which model sounds advanced?”

To:

> “Which model fits the problem constraints and user experience?”

---

## Architectural State at End of Day 3

The system now had:

- Clear domain (speaker comparison)
- Deterministic TOPSIS backbone
- Benefit vs cost handling
- Normalization strategy
- Penalty modeling idea
- Modular architecture plan
- No AI-based ranking logic

This was the first time the system felt mathematically grounded.

---

## Key Insight From Phase 2

A good decision system:

- Does not guess.
- Does not average blindly.
- Does not overcomplicate.

It:

- Normalizes.
- Weighs.
- Compares to ideal.
- Measures distance.
- Explains ranking transparently.

This became the core identity of the Speaker Decision Companion System.

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

### Context

By the end of Day 5, the system had:

- A mathematically validated TOPSIS engine.
- Penalty modeling logic.
- Clear benefit vs cost handling.
- Modular separation at conceptual level.

However, it was still an algorithm prototype.

Day 6 focused on transforming the engine into a structured, user-facing web application.

---

### Major Evolution

Shift from:

> Algorithm prototype

To:

> Full web application architecture

This phase required thinking beyond mathematics.

The challenge became:

- How will users input data?
- How will weights be adjusted?
- How do we reduce complexity?
- How do we prevent decision fatigue?

---

### Introduced Backend Architecture

Adopted FastAPI for backend implementation.

Structured modular design:

- `decision_engine.py` → Pure TOPSIS logic  
- `explanation_engine.py` → Deterministic explanation generation  
- `preprocessing.py` → Input transformation & normalization preparation  
- `config.py` → Criteria definitions & mappings  
- `main.py` → Routing & request handling  

This separation ensured:

- No mixing of UI and algorithm.
- Clean maintainability.
- Future extensibility.
- Testable logic layers.

---

### Integration with AntiGravity

AntiGravity was used to:

- Rapidly scaffold the web structure.
- Generate base templates.
- Structure routes and forms.

However:

- Core scoring logic remained manually designed.
- TOPSIS engine was not AI-generated blindly.
- I validated every architectural decision.

This maintained:

- Transparency.
- Deterministic control.
- Ownership of logic.

---

### Introduced User Segmentation

1. Casual Buyer  
2. Audio Enthusiast  
3. Technical Evaluator  

---

### Why Segmentation Emerged

While building forms, I realized:

Not all users think the same way.

From my own experience researching speakers for my car:

- Casual buyers care about battery, loudness, portability.
- Enthusiasts care about drivers, frequency range, codecs.
- Technical evaluators care about detailed specs and distortion.

If all criteria are shown to everyone:

- Decision fatigue increases.
- Cognitive overload occurs.
- Weight assignment becomes confusing.
- System becomes intimidating.

Thus segmentation was introduced.

---

### UX Architectural Insight

Different users need:

- Different levels of complexity.
- Different criteria exposure.
- Different explanation depth.
- Different default assumptions.

This was a shift from:

> Engineering-only thinking

To:

> User-centric architecture thinking

---

### Weight Configuration Evolution

Initially:

- Weights were numeric inputs.

Then evolved to:

- Separate weight adjustment page.
- Qualitative labels (Bad / Good / Top).
- Direction override (Benefit vs Cost).

This improved:

- Usability.
- Clarity.
- Control.
- Transparency.

---

### Input Handling Refinement

Special logic introduced:

- Extract numeric value from IP rating (e.g., IPX6 → 6).
- Charging type as filter or penalty (not weighted).
- Optional advanced fields.
- Multi-speaker dynamic comparison.

This phase strengthened preprocessing architecture.

---

### Mistakes & Corrections

Mistake:
- Initially tried to support all user types equally.
- Over-segmented into multiple modes.
- Risked unnecessary architectural complexity.

Correction:
- Later simplified to a stronger single deterministic core.
- Merged advanced criteria intelligently.
- Avoided over-fragmented routing.

---

### Architectural Outcome

At the end of Phase 5, the system became:

- A multi-page FastAPI web application.
- Deterministic TOPSIS-based backend.
- Role-aware criteria exposure.
- Modular file structure.
- Separate weight configuration logic.
- Configurable penalty system.
- Dynamic speaker comparison capability.

The system was no longer just an algorithm.

It became an application architecture.

---

### What Changed in My Thinking

Before Phase 5:
- I was engineering a ranking algorithm.

After Phase 5:
- I was architecting a decision-support platform.

This phase marked the transition from:

> Mathematical correctness

To:

> System design maturity.

## Phase 6 — Criteria Refinement & Penalty Modeling (Day 7)

### Context

By this stage, the system was fully functional:

- Multi-page FastAPI application
- Deterministic TOPSIS core
- Modular architecture
- User-adjustable weights
- Multi-speaker comparison

However, deeper refinement was still required.

This phase focused on improving realism, flexibility, and architectural cleanliness.

---

## Major Additions

### 1. Brand Reliability Penalty

Observation:

Some brands show noticeable clarity degradation after months of use.  
As a buyer researching speakers for my car, I encountered this concern frequently.

Architectural Response:

Introduced a configurable reliability multiplier applied **after TOPSIS scoring**.

This ensured:

- Core scoring remained mathematically pure.
- Real-world reliability was modeled transparently.
- Penalty was adjustable, not hardcoded.

---

### 2. Clarity Degradation Penalty

Certain speakers may sound excellent initially but degrade over time.

Instead of removing them entirely, I:

- Modeled degradation as a multiplier.
- Applied it post-TOPSIS.
- Allowed configuration.

This preserved determinism while incorporating lifecycle realism.

---

### 3. Battery Honesty Multiplier

Some manufacturers test battery life at 50–60% volume.

As a buyer, I identified this as misleading.

Design decision:

- Add a "battery honesty factor".
- Apply it as a multiplier after scoring.
- Keep penalty transparent in explanation output.

This prevented manipulation of ranking while maintaining mathematical clarity.

---

### 4. USB-C: Filter vs Preference Logic

Important architectural shift:

Charging type should NOT behave like a normal weighted criterion.

Instead, users may:

- Require USB-C → filter out speakers.
- Prefer USB-C → apply penalty.
- Ignore charging type.

This separated:

Hard constraints  
From  
Weighted preferences

This was a key maturity step in system modeling.

---

### 5. Direction-Overridable Attributes

Originally:

Price → cost  
Weight → cost  

But I realized:

Some users prefer heavier speakers (perceived sturdiness).  
Some users may prefer premium pricing (brand perception).

Thus I allowed users to override:

- Benefit
- Cost

At weight assignment stage.

This significantly improved flexibility without breaking the TOPSIS structure.

---

### 6. Separate Weight Adjustment Page

Initially, weights were part of the main input form.

Problem:

- Cognitive overload
- Cluttered UI
- Reduced clarity

Solution:

Separate "Adjust Criteria Importance" page.

This improved:

- Focused thinking
- Clean architecture
- Clear data flow
- UX separation of concerns

---

## Mature Design Features

| Feature | Architectural Reason |
|----------|---------------------|
| Benefit / Cost override | Support different user value systems |
| USB-C as filter | Distinguish constraint vs preference |
| Post-TOPSIS penalty multiplier | Preserve deterministic purity |
| Explanation engine | Ensure transparency and auditability |
| Weight separation page | Improve cognitive clarity |
| Optional advanced fields | Reduce decision fatigue |

---

## Final Core Engine Pipeline

```
User Input
    ↓
Preprocess & Type Conversion
    ↓
Decision Matrix Construction
    ↓
Normalization
    ↓
Apply Weights
    ↓
Compute Ideal Best & Worst
    ↓
Euclidean Distance
    ↓
TOPSIS Closeness Score
    ↓
Apply Penalty Multipliers
    ↓
Rank
    ↓
Generate Deterministic Explanation
```

---

## Architectural Maturity Achieved

At this point, the system achieved:

- Deterministic mathematical core
- Flexible attribute modeling
- Post-scoring penalty system
- Separation of constraint vs preference
- User-controlled direction overrides
- Modular FastAPI architecture
- Transparent explanation engine
- No black-box AI scoring

---

## Thinking Evolution at This Stage

Earlier:
> Build a ranking algorithm.

Now:
> Build a flexible, real-world decision modeling system.

This phase finalized the system as:

A penalty-aware, direction-flexible, user-adjustable TOPSIS-based decision architecture.

The design was no longer experimental.

It was structured, explainable, and mature.
## Phase 7 — Architectural Simplification (Day 7)

### Realization

The introduction of three separate modes (Casual / Enthusiast / Technical) increased architectural and routing complexity without proportionate value.

Although segmentation initially reduced cognitive overload, it introduced:

- Multiple routing branches
- Repeated criteria configuration
- Higher maintenance complexity
- Risk of inconsistent scoring logic

The core decision engine remained identical across modes.

This indicated architectural redundancy.

---

### Decision

- Remove Enthusiast mode.
- Merge strong technical criteria into a single refined system.
- Keep advanced criteria optional rather than mode-specific.

This preserved:

- Flexibility
- Scalability
- Simplicity
- Maintainability

---

### Added / Finalized Missing Criteria

To strengthen the unified model, the following criteria were incorporated or formalized:

- Mic support
- Physical Weight
- Price
- Bass scale (structured scale instead of vague label)
- Battery size (optional)
- Battery tested loudness (optional realism indicator)
- Frequency range (advanced)
- Warranty (Years)
- App Support
- Number of Drivers
- Stand Orientation

This ensured the system remained technically strong without fragmentation.

---

### System Became

> A modular deterministic TOPSIS engine  
> with configurable penalties  
> with benefit/cost flexibility  
> with structured UI flow  

The architecture stabilized.

Complexity was now intentional, not accidental.

---

# Final Architecture

## 1️⃣ Backend

- FastAPI
- Modular structure
- No AI-based ranking
- Deterministic scoring

### Core Modules

- `decision_engine.py` → TOPSIS logic  
- `preprocessing.py` → Data cleaning & transformation  
- `explanation_engine.py` → Rule-based reasoning  
- `config.py` → Criteria & penalty configurations  
- `main.py` → Routing & flow control  

The TOPSIS engine remains framework-independent.

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

This pipeline remains deterministic.

No probabilistic or AI inference is involved.

---

## 3️⃣ Penalty Architecture

Penalties are applied AFTER scoring:

```
Final Score = TOPSIS Score × BatteryHonesty × BrandFactor × DegradationFactor
```

This preserves:

- Mathematical clarity
- Separation of scoring vs realism modeling
- Transparent adjustment logic

---

## 4️⃣ UX Flow

Landing Page  
→ Select User Type  
→ Enter Speakers  
→ Adjust Weights  
→ Apply Filters (USB-C etc.)  
→ View Ranked Results  
→ Explanation Breakdown  

Clear separation between:

- Data input
- Weight configuration
- Constraint application
- Result interpretation

---

## 5️⃣ Key Design Trade-offs

| Decision | Trade-off |
|----------|------------|
| Not using AI ranking | Lose adaptive learning, gain transparency |
| Not relying on scraping | Lose automation, gain stability |
| TOPSIS over AHP | Lose subjective hierarchy modeling, gain scalability |
| Penalty multiplier instead of embedding inside matrix | Cleaner separation of concerns |
| Remove Enthusiast mode | Simpler architecture |

---

# Edge Cases Considered

- All speakers filtered out by USB-C requirement
- Missing distortion data
- Missing battery test volume
- Non-monotonic attributes
- User overriding cost/benefit
- Less than 2 speakers entered
- Invalid numeric inputs
- Optional advanced fields left empty

The system remains stable under incomplete input scenarios.

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
---

# BUILD_PROCESS.md

Project: Speaker Decision Companion System  
Author: Pranav Das  
Core Model: Deterministic TOPSIS-based MCDA  

---

## 1. How I Started

The assignment required building a Decision Companion System that:

- Accepts multiple options  
- Accepts multiple criteria with different importance  
- Produces a ranked output  
- Explains why a decision was made  
- Does not rely entirely on AI  

Initially, I approached this as a classical Multi-Criteria Decision Analysis (MCDA) problem.

Simultaneously, I was personally researching Bluetooth speakers for my car for nearly 5–6 days.  
As a buyer, I had already explored:

- Battery performance claims
- Real-world loudness
- Brand reliability
- Charging types
- Build durability

This real-world context influenced the project direction.

I decided to build not just as a developer — but as a user.

---

## 2. Model Selection

After evaluating:

- Weighted Scoring Model  
- AHP (Analytic Hierarchy Process)  
- MCDA frameworks  
- TOPSIS  

I selected TOPSIS because:

- It naturally handles both benefit and cost criteria  
- It ranks alternatives based on distance from ideal best and worst  
- It is mathematically deterministic  
- It is explainable (no black-box behavior)  
- It scales well with multiple speakers  

---

## 3. Initial Architecture Plan

The first architectural design separated:

- Decision Engine (TOPSIS)
- Explanation Engine
- Preprocessing Layer
- FastAPI Web Layer

This ensured:

- No business logic inside routes  
- Deterministic scoring  
- Clean modular structure  
- Easy refactoring  

The TOPSIS engine was intentionally kept framework-independent.

---

## 4. Early Feature Expansion (Over-Engineering Phase)

Initially, I introduced:

- Multiple user modes (Casual / Enthusiast)  
- Advanced penalty stacking  
- Brand reliability multipliers  
- Battery honesty controls  
- Clarity degradation factors  

Although technically interesting, I later realized:

- They increased cognitive load  
- They expanded scope beyond assignment requirements  
- They reduced clarity of the core system  

This phase taught me the trade-off between feature richness and architectural clarity.

---

## 5. Refactoring & Scope Reduction

After reviewing the structure, I simplified the system to focus on:

- One primary unified mode  
- Strong but meaningful criteria  
- Clear cost/benefit categorization  
- Explicit weight normalization  
- Controlled constraint modeling (USB-C logic)  

I removed:

- Separate Enthusiast routing branches  
- Overlapping configuration layers  
- Redundant complexity  

This reduced architectural noise while preserving modeling depth.

---

## 6. Criteria Design Evolution

### Phase 1 — Technical Spec Heavy

Initially focused heavily on raw specifications:

- Bluetooth version  
- Frequency response  
- Driver size  
- Codec types  

This proved unsuitable for general users.

### Phase 2 — Outcome-Based Criteria

I restructured criteria into:

- Sound Clarity  
- Bass Strength  
- Loudness  
- Battery Life  
- Portability  
- Build Quality  
- IP Rating  
- Price  
- Physical Weight  
- Brand Reliability  
- App Support  
- Warranty  
- Stand Orientation  

This balanced usability with technical depth.

---

## 7. Cost vs Benefit Classification

TOPSIS requires explicit categorization:

Benefit → Higher is better  
Cost → Lower is better  

Final cost criteria:

- Price  
- Physical Weight  

All others default to benefit.

Selected criteria allow user override.

---

## 8. Charging Type Modeling Decision

Charging Type (USB-C) is not treated as a weighted criterion.

Instead:

- Must Be USB-C → Pre-TOPSIS filtering  
- Prefer USB-C → Post-score penalty  
- Don’t Care → Ignored  

This cleanly separates:

Constraint logic  
Preference logic  
Performance scoring  

---

## 9. Weight Normalization

Users assign importance on a 1–5 scale.

Before TOPSIS:

wi = wi / Σw

This ensures:

- Proper normalization  
- No artificial bias  
- Stable ranking  

---

## 10. Explanation Engine

The explanation engine:

- Identifies top contributing criteria  
- Highlights weaknesses  
- Reports applied penalties  
- Produces deterministic textual reasoning  

No generative AI is used.

All explanations are derived from computed metrics.

---

## 11. Mistakes & Corrections

### Mistake 1 — Over-Expanding Modes

Initially introduced multiple user personas.  
Correction: Reduced to a unified system with optional advanced criteria.

### Mistake 2 — Penalty Stacking Complexity

Advanced multipliers increased complexity without proportional benefit.  
Correction: Simplified to essential, explainable multipliers.

### Mistake 3 — Treating All Criteria Equally

Charging type was initially weighted like other criteria.  
Correction: Modeled it as constraint + soft penalty instead.

---

## 12. Final Architecture

FastAPI Routes  
      ↓  
Preprocessing Layer  
      ↓  
TOPSIS Decision Engine  
      ↓  
Explanation Engine  
      ↓  
Result Rendering  

### Key Principles

- Deterministic logic  
- Transparent scoring  
- Modular separation  
- Minimal scope creep  
- Clear mathematical foundation  

---

## 13. What I Would Improve With More Time

- Replace in-memory session storage with persistent session management  
- Add structured product dataset ingestion  
- Add visual contribution graphs  
- Add preset decision profiles (Battery-focused, Party-focused, etc.)  
- Add confidence modeling for missing attributes  
- Introduce optional Audio Enthusiast expansion layer  
- Add dynamic MCDA model switching if criteria count changes  

---

## 14. Final Reflection

The biggest learning was not about implementing TOPSIS.

It was about:

- Structuring ambiguity  
- Balancing realism with mathematical purity  
- Preventing scope creep  
- Designing for both developer clarity and user cognition  
- Knowing when to simplify  

This project evolved from:

> "Build a ranking tool"

Into:

> "Design a deterministic, explainable, user-aware decision architecture."

I built it as both:

A system designer  
And  
A real buyer evaluating speakers.
