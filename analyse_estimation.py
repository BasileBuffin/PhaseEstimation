import qsharp
from PhaseEstimation import run

n_shots = 10
phi = 0
n_oracle = 1

result = run.simulate(nShots=n_shots, phi=phi, oraclePower=n_oracle)

print(result)


