#####################################################
#   Showcase of different types of algorithms:      #
#       - Brute Force   -> Deterministic            #
#       - Monte Carlo   -> Nondeterministic         #
#       - Heuristic     -> Deterministic            #
#                                                   #
#   Author: Erik Boháč                              #
#####################################################

from boat_algorithms import boat_brute_force, boat_monte_carlo, boat_heuristic

print(boat_brute_force(73, 85, 81))
print(boat_monte_carlo(73, 85, 81))
print(boat_heuristic(73, 85, 81))
