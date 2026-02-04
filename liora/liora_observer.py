#!/usr/bin/env python3
"""
LIORA MODULE v1.2 - Identity Coherence Sentinel
-----------------------------------------------
Author: Ilion Project Architecture
Purpose: Non-generative observation of semantic identity drift.
Mechanism: Compares current identity vector against origin TII.
Decision rule: instant geometric deviation (no temporal smoothing).
Auxiliary metrics: optional sliding window (diagnostic only).
"""

import numpy as np
from scipy.spatial.distance import cosine
import json
from datetime import datetime, timezone
import argparse
import logging
import sys
import hashlib
from collections import deque


# -------------------------------------------------
# Logging (Audit Trail)
# -------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [LIORA] - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("liora_audit.log"),
        logging.StreamHandler(sys.stdout)
    ]
)


# -------------------------------------------------
# Helpers
# -------------------------------------------------

def normalize(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=np.float64)
    n = np.linalg.norm(v)
    if n == 0.0:
        raise ValueError("Zero vector detected during normalization.")
    return v / n


def stable_vector_hash(v: np.ndarray) -> str:
    v = np.ascontiguousarray(np.asarray(v, dtype=np.float64))
    return hashlib.sha256(v.tobytes()).hexdigest()


# -------------------------------------------------
# LIORA Sentinel
# -------------------------------------------------

class LioraSentinel:

    def __init__(self, origin_tii, threshold=0.15, window_size=5):
        """
        :param origin_tii: canonical identity vector (TII origin)
        :param threshold: cosine distance threshold
        :param window_size: sliding window size (diagnostic only)
        """

        self.origin_tii = normalize(origin_tii)
        self.threshold = float(threshold)

        self.origin_hash = stable_vector_hash(self.origin_tii)

        self.history = []
        self.recent_drifts = deque(maxlen=window_size)

        logging.info("Liora Sentinel ACTIVATED")
        logging.info(f"Threshold: {self.threshold}")
        logging.info(f"Origin TII hash: {self.origin_hash}")

    def observe(self, current_tii, timestep_id=None):
        """
        Passive observation.
        Does NOT modify identity.
        """

        current_tii = normalize(current_tii)

        drift = cosine(self.origin_tii, current_tii)

        self.recent_drifts.append(drift)
        avg_drift = float(np.mean(self.recent_drifts))

        is_safe = drift <= self.threshold
        status = "COHERENT" if is_safe else "DRIFT_ALERT"

        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "step_id": timestep_id,
            "drift_raw": round(float(drift), 6),
            "drift_avg": round(avg_drift, 6),  # diagnostic only
            "threshold": self.threshold,
            "status": status,
            "origin_hash": self.origin_hash,
            "action_required": not is_safe
        }

        self.history.append(event)

        if is_safe:
            logging.info(
                f"Step {timestep_id}: OK | drift={drift:.5f} avg={avg_drift:.5f}"
            )
            return True, drift, avg_drift
        else:
            logging.warning(
                f"Step {timestep_id}: *** DRIFT ALERT *** | drift={drift:.5f} avg={avg_drift:.5f}"
            )
            return False, drift, avg_drift

    def export_report(self, filename="liora_report.json"):

        report = {
            "meta": {
                "module": "Liora Identity Observer",
                "version": "1.2",
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "origin_hash": self.origin_hash,
                "threshold": self.threshold
            },
            "audit_trail": self.history
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)

        logging.info(f"Audit report written to {filename}")


# -------------------------------------------------
# Demo / Simulation
# -------------------------------------------------

def simulate_semantic_entropy(tii_origin, steps=10):

    sentinel = LioraSentinel(
        origin_tii=tii_origin,
        threshold=0.15,
        window_size=5
    )

    current = normalize(tii_origin).copy()

    rng = np.random.default_rng(42)

    print("\n--- STARTING LIORA OBSERVATION LOOP ---\n")

    for t in range(1, steps + 1):

        noise = rng.normal(0.0, 0.02, size=current.shape)

        factor = 0.3 if t < 6 else 0.9
        current = normalize(current + factor * noise)

        ok, drift, avg = sentinel.observe(current, timestep_id=t)

        if not ok:
            print(">>> [SYSTEM NOTICE] Identity drift detected")

    sentinel.export_report()
    print("\n--- END OBSERVATION ---")


# -------------------------------------------------
# CLI
# -------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="LIORA – Identity Coherence Sentinel"
    )

    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run built-in drift simulation"
    )

    args = parser.parse_args()

    if args.demo:
        # example abstract identity vector
        TII_ORIGIN = np.array([0.85, 0.90, 0.40, 0.99], dtype=np.float64)
        simulate_semantic_entropy(TII_ORIGIN, steps=12)
    else:
        print("Run with --demo to execute the LIORA simulation.")


if __name__ == "__main__":
    main()
