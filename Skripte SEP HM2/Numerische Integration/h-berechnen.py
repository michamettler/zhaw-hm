import math

# Gegebene Werte
pi = math.pi
max_error = 1e-3

# Berechnung der minimalen Anzahl der Intervalle n
n_min = math.sqrt(pi**3 / (12 * max_error))

# Schrittweite h berechnen
h_max = pi / n_min

print(f"Die maximale Schrittweite h, um den Fehler kleiner als 10^-3 zu halten, beträgt: {h_max:.6f}")
