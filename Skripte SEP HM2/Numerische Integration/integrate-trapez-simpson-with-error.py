import numpy as np

# SUMMIERTE TRAPEZREGEL

# Implementation
def sum_trapez(f, a, b, h):
    n = int((b - a) / h)
    T = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        T = T + f(x)
    T = h * T
    return T, n

def sum_simpson(f, a, b, h):
    n = int((b - a) / h)
    S = f(a) + f(b) + 4 * f(a + h / 2)
    for i in range(1, n):
        x = a + i * h
        S = S + 2 * f(x) + 4 * f(x + h / 2)
    S = h / 6 * S
    return S

# Berechnung der maximalen Schrittweite h
def max_schrittweite(f, f_second_derivative, a, b, max_error):
    max_f_second_derivative = np.max(np.abs(f_second_derivative(np.linspace(a, b, 1000))))
    n_min = np.sqrt((b - a)**3 * max_f_second_derivative / (12 * max_error))
    return (b - a) / n_min

# Beispiel-Funktion
def f(x):
    return np.sin(x)

# Zweite Ableitung der Beispiel-Funktion
def f_second_derivative(x):
    return -np.sin(x)

# Parameter
a = 0.
b = np.pi
I = 2  # Exakter Wert des Integrals
max_error = 1e-3  # Gewünschte Genauigkeit

# Berechne maximale Schrittweite
h_max = 0.0618

# Trapezregel anwenden mit maximaler Schrittweite
T, n_iterations = sum_trapez(f, a, b, h_max)
print(f"Die maximale Schrittweite h beträgt: {h_max:.6f}")
print(f"Die Näherung des Integrals mit der Trapezregel beträgt: {T:.6f}")
print(f"Der Fehler beträgt: {np.abs(T - I):.6f}")
print(f"Anzahl der Iterationen: {n_iterations}")

# Teste verschiedene Schrittweiten
kmax = 5
print("\nTest mit verschiedenen Schrittweiten:")
print("h       T(h)                    |T(h) - I| (absolute error)    Iterationen")
for k in range(0, kmax + 1):
    h = 10**(-k)
    T, n_iterations = sum_trapez(f, a, b, h)
    print(f"{h:.6f} {T:.15f} {np.abs(T - I):.15f} {n_iterations}")
