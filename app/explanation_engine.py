"""
explanation_engine.py — Rule-based explanation engine.

This module generates deterministic, rule-based text explanations
for ranking results. No LLM or AI is involved.

DO NOT add FastAPI dependencies to this module.
"""


def generate_explanation(speaker, score, weighted_matrix_row, criteria, ideal_best):

    contributions = {}
    weaknesses = {}

    for i, c in enumerate(criteria):
        contributions[c.name] = weighted_matrix_row[i]
        weaknesses[c.name] = (weighted_matrix_row[i] - ideal_best[i]) ** 2

    # Top strengths
    top_strengths = sorted(contributions.items(), key=lambda x: x[1], reverse=True)[:3]

    # Weakest areas
    top_weaknesses = sorted(weaknesses.items(), key=lambda x: x[1], reverse=True)[:2]

    explanation = f"\nSpeaker: {speaker.name}\n"
    explanation += f"Final Score: {round(score, 4)}\n\n"

    explanation += "Strengths:\n"
    for s in top_strengths:
        explanation += f"- Strong performance in {s[0]}\n"

    explanation += "\nAreas Further From Ideal:\n"
    for w in top_weaknesses:
        explanation += f"- Could improve in {w[0]}\n"

    if speaker.battery_test_volume < 80:
        explanation += f"\nBattery penalty applied (tested at {speaker.battery_test_volume}% volume).\n"

    return explanation
