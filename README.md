# 🔊 Vonnue — Speaker Decision Companion

A deterministic speaker ranking web app powered by the **TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) multi-criteria decision algorithm.

Compare portable/Bluetooth speakers side-by-side across **18 weighted criteria** and get an objective, score-based ranking.

---

## ✨ Features

- **Multi-speaker comparison** — add 2 or more speakers dynamically
- **18 evaluation criteria** — price, weight, clarity, bass, wattage, battery, IP rating, Bluetooth, drivers, warranty, brand reliability, app support, stand orientation, and more
- **User-adjustable weights** — set importance (1–5) for each criterion
- **Direction override** — choose "Higher is Better" or "Lower is Better" for Price & Weight
- **Charging type constraint** — filter or penalise non-USB-C speakers
- **TOPSIS engine** — normalised decision matrix, ideal/anti-ideal solutions, closeness scoring
- **AI-generated explanations** — strengths and weaknesses for each speaker

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **pip**

### Clone & Install

```bash
git clone https://github.com/Pranavdas-1/Vonnue.git
cd Vonnue
pip install -r requirements.txt
```

### Run

```bash
python -m uvicorn app.main:app --reload --port 8000
```

Open **http://127.0.0.1:8000** in your browser.

---

## 📁 Project Structure

```
Vonnue/
├── app/
│   ├── __init__.py
│   ├── config.py              # Criteria keys, types, labels, icons
│   ├── decision_engine.py     # TOPSIS algorithm (do not modify)
│   ├── explanation_engine.py  # Strength/weakness text generator
│   ├── main.py                # FastAPI routes
│   ├── preprocessing.py       # Form → Speaker/Criterion conversion
│   ├── static/                # Static assets
│   └── templates/             # Jinja2 HTML templates
│       ├── base_casual.html
│       ├── casual_speakers.html
│       ├── casual_weights.html
│       └── casual_results.html
└── requirements.txt
```

---

## 🛠 Tech Stack

| Layer      | Technology       |
|------------|------------------|
| Backend    | FastAPI + Uvicorn |
| Templating | Jinja2            |
| Algorithm  | TOPSIS (NumPy)    |
| Frontend   | Vanilla HTML/CSS/JS |

---

## 📝 License

This project is for educational and personal use.
