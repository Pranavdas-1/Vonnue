"""
decision_engine.py — TOPSIS decision engine.

This module contains the core TOPSIS scoring logic.
It is kept independent from FastAPI; routes call functions
defined here without embedding any scoring logic in the routes.

DO NOT add FastAPI dependencies to this module.
"""

import numpy as np
from typing import List, Dict


class Criterion:
    def __init__(self, name: str, weight: float, criterion_type: str):
        """
        criterion_type: 'benefit' or 'cost'
        """
        self.name = name
        self.weight = weight
        self.criterion_type = criterion_type


class Speaker:
    def __init__(self, name: str, attributes: Dict[str, float], battery_test_volume: float = 80):
        """
        attributes: {criterion_name: value}
        battery_test_volume: % volume at which battery was tested
        """
        self.name = name
        self.attributes = attributes
        self.battery_test_volume = battery_test_volume


class TOPSISDecisionEngine:
    def __init__(self, criteria: List[Criterion], penalty_alpha: float = 0.3):
        self.criteria = criteria
        self.penalty_alpha = penalty_alpha

    # -----------------------------
    # STEP 1: Build Decision Matrix
    # -----------------------------
    def _build_matrix(self, speakers: List[Speaker]):
        matrix = []
        for sp in speakers:
            row = [sp.attributes[c.name] for c in self.criteria]
            matrix.append(row)
        return np.array(matrix, dtype=float)

    # -----------------------------
    # STEP 2: Normalize (Vector)
    # -----------------------------
    def _normalize(self, matrix):
        norm = np.sqrt((matrix ** 2).sum(axis=0))
        # Avoid division by zero for columns where all values are 0
        norm[norm == 0] = 1
        return matrix / norm

    # -----------------------------
    # STEP 3: Apply Weights
    # -----------------------------
    def _apply_weights(self, normalized_matrix):
        weights = np.array([c.weight for c in self.criteria])
        return normalized_matrix * weights

    # -----------------------------
    # STEP 4: Ideal Best & Worst
    # -----------------------------
    def _ideal_solutions(self, weighted_matrix):
        ideal_best = []
        ideal_worst = []

        for j, c in enumerate(self.criteria):
            column = weighted_matrix[:, j]

            if c.criterion_type == "benefit":
                ideal_best.append(column.max())
                ideal_worst.append(column.min())
            else:  # cost
                ideal_best.append(column.min())
                ideal_worst.append(column.max())

        return np.array(ideal_best), np.array(ideal_worst)

    # -----------------------------
    # STEP 5: Distance Calculation
    # -----------------------------
    def _distance(self, weighted_matrix, ideal_best, ideal_worst):
        dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
        dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))
        return dist_best, dist_worst

    # -----------------------------
    # STEP 6: Relative Closeness
    # -----------------------------
    def _closeness(self, dist_best, dist_worst):
        return dist_worst / (dist_best + dist_worst)

    # -----------------------------
    # STEP 7: Battery Cheating Penalty
    # -----------------------------
    def _battery_penalty(self, speaker: Speaker):
        if speaker.battery_test_volume >= 80:
            return 1.0

        cheat_factor = (80 - speaker.battery_test_volume) / 80
        reliability = 1 - self.penalty_alpha * cheat_factor
        return reliability

    # -----------------------------
    # PUBLIC METHOD: Evaluate
    # -----------------------------
    def evaluate(self, speakers: List[Speaker]):

        matrix = self._build_matrix(speakers)
        normalized = self._normalize(matrix)
        weighted = self._apply_weights(normalized)

        ideal_best, ideal_worst = self._ideal_solutions(weighted)
        dist_best, dist_worst = self._distance(weighted, ideal_best, ideal_worst)

        closeness = self._closeness(dist_best, dist_worst)

        # Apply penalty
        final_scores = []
        for i, sp in enumerate(speakers):
            penalty_multiplier = self._battery_penalty(sp)
            final_scores.append(closeness[i] * penalty_multiplier)

        ranking = sorted(
            zip(speakers, final_scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranking, weighted, ideal_best
