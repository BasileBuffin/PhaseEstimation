import numpy as np
import qsharp
from scipy.stats import linregress
from utils import *


phi = 0

"""
Variable: number of shots
"""

shots = [i for i in range(1, 101)]
precisionForNShots = average_precision_for_n_shots(shots=shots, phi=phi, oraclePower=1, n=10)
show_simple_plot(shots, precisionForNShots, 'n Shots', 'Precision', 'Precision for a Variation of the Number of Shots')

"""
Variable: number of oracles
"""

oracles = [i for i in range(1, 101)]
precisionForNOracles = average_precision_for_n_oracles(shots=10, phi=phi, oraclePower=oracles, n=10)
show_simple_plot(shots, precisionForNOracles, 'n Oracles', 'Precision', 'Precision for a Variation of the Number of Oracles')

"""
Fit (shots)
"""

log_shots = np.log(np.array(shots))
log_precisionForNShots = np.log(np.array(precisionForNShots))

slope, intercept, r_value, p_value, std_err = linregress(log_shots, log_precisionForNShots)
print("=====")
print("Linear Regression For Shot Variation")
print("=====")
print("slope = ", slope)
show_simple_plot(log_shots, log_precisionForNShots, 'log(n Shots)', 'log(f(n Shots))', 'Linear Regression For Shot Variation')

"""
Fit (oracles)
"""

log_shots = np.log(np.array(shots))
log_precisionForNOracles = np.log(np.array(precisionForNOracles))

slope, intercept, r_value, p_value, std_err = linregress(log_shots, log_precisionForNOracles)
print("=====")
print("Linear Regression For Oracle Variation")
print("=====")
print("slope = ", slope)
show_simple_plot(log_shots, log_precisionForNOracles, 'log(n Oracles)', 'log(f(n Oracles))', 'Linear Regression For Oracle Variation')
