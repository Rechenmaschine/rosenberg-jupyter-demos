"""Shared test signal for the filter demos: a simulated noisy model-rocket altitude trace."""
import numpy as np


def generate():
    """Return (t, true_sig): a clean simulated rocket altitude trace at 50 Hz."""
    g, a_boost, t_burn = 9.81, 80, 0.8
    t = np.arange(0, 15, 0.02)
    boost = t <= t_burn
    true_sig = np.empty_like(t)
    true_sig[boost] = 0.5 * (a_boost - g) * t[boost] ** 2
    h_burn = 0.5 * (a_boost - g) * t_burn ** 2
    v_burn = (a_boost - g) * t_burn
    tc = t[~boost] - t_burn
    true_sig[~boost] = h_burn + v_burn * tc - 0.5 * g * tc ** 2
    true_sig = np.maximum(true_sig, 0)
    end = np.where((true_sig == 0) & (t > t_burn))[0]
    if len(end):
        t, true_sig = t[:end[0] + 1], true_sig[:end[0] + 1]
    return t, true_sig
