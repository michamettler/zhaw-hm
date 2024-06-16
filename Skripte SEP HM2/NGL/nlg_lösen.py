import numpy as np
from scipy.optimize import fsolve

# Definieren der Gleichungen basierend auf der Aufgabenstellung
def equations(vars):
    x, y = vars
    eq1 = 16 * x**2 - (x**2 + 1) * (x + y)**2  # Von der gegebenen Gleichung für die 4m Leiter
    eq2 = 9 * y**2 - (y**2 + 1) * (x + y)**2  # Von der gegebenen Gleichung für die 3m Leiter
    return [eq1, eq2]

# Anfangsschätzung für die Variablen x und y
initial_guess = [1, 1]

# Verwenden von fsolve, um die Wurzel der Gleichungen zu finden
solution = fsolve(equations, initial_guess)

x, y = solution

print(f'Lösung: x = {x:.4f} Meter, y = {y:.4f} Meter')
