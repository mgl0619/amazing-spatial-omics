"""Generate the simulated tier.

This is the only tier where the right answer is known, which makes it the only place a
reader can measure how far their estimate landed from the truth. Every generator here
returns both the data and the ground truth that produced it.

Keep these tiny and deterministic: seeded, committed, and fast enough to run in CI.
"""

import numpy as np


def simulate_tissue(n_cells: int = 2000, seed: int = 0):
    """Return (data, truth). Truth is not optional — it is the point of this tier."""
    rng = np.random.default_rng(seed)
    raise NotImplementedError("TODO")


def simulate_null_tissue(n_cells: int = 2000, seed: int = 0):
    """Spatially structured tissue with NO true expression signal.

    Used by lesson 9: any test that returns significant genes here is miscalibrated.
    """
    rng = np.random.default_rng(seed)
    raise NotImplementedError("TODO")


def simulate_segmentation_truth(n_cells: int = 500, seed: int = 0):
    """Cells with known boundaries, for measuring chimera rate in lesson 4."""
    rng = np.random.default_rng(seed)
    raise NotImplementedError("TODO")
