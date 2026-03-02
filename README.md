# Speaker Decision Companion

A deterministic web-based Decision Companion System for ranking Bluetooth / portable speakers using the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) multi-criteria decision algorithm.

The system compares multiple speakers across structured, weighted criteria and produces an objective, explainable ranking.

### Live Demo:
👉 https://vonnue.onrender.com/

📌 Repository Notes

The initial development repository with early commit history was deleted during restructuring.

Current repositories:

Main Application:
👉 https://github.com/Pranavdas-1/Vonnue.1

Standalone TOPSIS Development:
👉 https://github.com/Pranavdas-1/Topsis_algorithm

The current repository contains the final structured implementation.

### Problem Statement
Choosing a speaker involves multiple trade-offs:

Price vs Performance
Battery Life vs Loudness
Portability vs Durability
Feature Set vs Build Quality
Most buying decisions rely on subjective reviews.

It structures this decision mathematically, allowing users to:

Compare multiple speakers
Assign importance to criteria
Get deterministic, explainable rankings

## Core Features

🔹 Multi-Speaker Comparison

Add 2 or more speakers dynamically and compare them side-by-side.

🔹 18 Evaluation Criteria

Includes:
Price (Cost)
Physical Weight (Cost)
Sound Clarity
Bass Strength
Output Power (Wattage)
Battery Life
Battery Size (optional)
IP Rating
Bluetooth Version
Number of Drivers
Warranty (Years)
Brand Reliability
App Support
Stand Orientation
Microphone Support
Charging Wattage
Multi-Pairing Support
USB-C Preference Logic

🔹 User-Adjustable Weights

Set importance (1–5 scale) for each criterion.
Weights are normalized before TOPSIS evaluation.

🔹 Direction Override

For selected criteria (e.g., Price, Weight), users can choose:
Higher is Better
Lower is Better

🔹 Charging Type Constraint

Users may:
Require USB-C (filters speakers)
Prefer USB-C (penalizes non-USB-C)
Ignore charging type

🔹 Deterministic TOPSIS Engine

Steps:

Construct decision matrix -> Normalize matrix -> Apply weights -> Compute ideal best & worst -> Calculate Euclidean distances -> Compute closeness coefficient -> Rank speakers

No AI is used in scoring.

🔹 Explanation Engine

Strengths and weaknesses are generated directly from weighted contributions.
Fully deterministic — no black-box outputs.

🏗 Architecture Overview

FastAPI Routes
        ↓
Preprocessing Layer
        ↓
TOPSIS Decision Engine
        ↓
Explanation Engine
        ↓
Result Rendering

📦 Clone Repository

Main Web Application:

git clone https://github.com/Pranavdas-1/Vonnue.1
cd Vonnue.1
pip install -r requirements.txt

Standalone TOPSIS development repository:

https://github.com/Pranavdas-1/Topsis_algorithm
▶️ Run Locally
python -m uvicorn app.main:app --reload --port 8000

Open in browser:

http://127.0.0.1:8000
🌐 Hosted Version

Deployed on Render:

👉 https://vonnue.onrender.com/

🛠 Tech Stack
Layer	Technology
Backend	FastAPI
Server	Uvicorn
Algorithm	TOPSIS (NumPy)
Templates	Jinja2
Frontend	HTML / CSS / Vanilla JS
Hosting	Render

📚 Decision Model Details

Each speaker is modeled as an n-dimensional vector.

The system evaluates speakers based on:

𝐶𝑖 = 𝐷− / (D+ - D-)​

Where:
𝐷+ = Distance from ideal best
𝐷- = Distance from ideal worst

Speakers closer to the ideal best receive higher scores.


Help you prepare for technical defense questions

Tell me what you want to finalize next.
