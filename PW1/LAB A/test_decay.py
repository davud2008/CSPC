"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
def test_rejects_negtive_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)
#   Check that calling simulate(...) with a negative lam raises a ValueError.
#   Which pytest tool checks that an error is raised?


# TODO 2: test_matches_law
def test_matches_law():
    N0 = 1000
    lam = 0.4
    dt = 0.05
    steps = 20

    results = []

    for seed in range(100):
        result = simulate(N0, lam, dt, steps, seed)
        results.append(result[-1])

    average = np.mean(results)

    expected = N0 * np.exp(-lam * dt * steps)

    assert average == pytest.approx(expected, rel=0.05)
#   Check that the simulation's AVERAGE over many seeds is close to the
#   physical law  N0 * exp(-lam * t).
#   Which pytest tool compares floating-point values with a tolerance?