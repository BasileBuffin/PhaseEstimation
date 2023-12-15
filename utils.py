import matplotlib.pyplot as plt
import numpy as np
import qsharp
from PhaseEstimation import run


"""
run simulations utils
"""

def get_precision(runResults, nShots, nOracles, phi):
    experimentalProbaOnes = runResults[1] / nShots
    experimentalPhi = (2 / nOracles) * (np.arcsin(np.sqrt(experimentalProbaOnes)) - (np.pi/4))
    return abs(experimentalPhi - phi)

def average_precision_of_n_runs(nShots, phi, oraclePower, n=1):
    precisions = []
    for i in range(n):
        runResults = run.simulate(nShots=nShots, phi=phi, oraclePower=oraclePower)
        precisions.append(get_precision(runResults, nShots, oraclePower, phi))

    return np.mean(precisions)

def average_precision_for_n_shots(shots, phi, oraclePower, n=1):
    precisionForNShots = []
    for nShots in shots:
        precision = average_precision_of_n_runs(nShots=nShots, phi=phi, oraclePower=oraclePower, n=n)
        precisionForNShots.append(precision)
    return precisionForNShots

def average_precision_for_n_oracles(shots, phi, oraclePower, n=1):
    precisionForNOracles = []
    for nOracles in oraclePower:
        precision = average_precision_of_n_runs(nShots=shots, phi=phi, oraclePower=nOracles, n=n)
        precisionForNOracles.append(precision)
    return precisionForNOracles



"""
plot utils
"""

def show_simple_plot(xs, ys, xlabel="", ylabel="", title=""):
    plt.plot(xs, ys)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
