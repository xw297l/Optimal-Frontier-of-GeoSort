# Optimal-Frontier-of-GeoSort
constants.py and offline_simulations_example.ipynb are folked from https://github.csnzoo.com/nj076v/substitution-offline-simulation/tree/subv15 with minor modification to generate all the .pkl files.
Opt_reg20.ipynb generates optimal frontier for GeoSort without substitution. 
Opt_varA.ipynb generates optimal frontier for GeoSort with substitution. It needs further modification in optimization constraints regarding number of candidates.
model.lp is the optimization model file of Opt_reg20.ipynb for solver gurobi.
