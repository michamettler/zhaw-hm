import numpy as np
import matplotlib.pyplot as plt

# Gegebene Daten
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0.54, 0.44, 0.28, 0.18, 0.12, 0.08])

# Transformation der Daten
y_prime = 1 / y

# Designmatrix A
A = np.vstack([np.ones_like(x), x**2]).T

# Normalgleichung lösen
# A^T A
ATA = np.dot(A.T, A)

# A^T y'
ATy_prime = np.dot(A.T, y_prime)

# Parameter berechnen
params = np.linalg.solve(ATA, ATy_prime)
a, b = params

# Berechnung der vorhergesagten Werte
y_prime_pred = a + b * x**2

# Berechnung des Fehlerfunktionals
E = np.sum((y_prime - y_prime_pred)**2)

# Originale nichtlineare Funktion
def original_model(x, a, b):
    return 1 / (a + b * x**2)

# Generierung von x-Werten für den Plot
x_fit = np.linspace(0, 5, 100)
y_fit = original_model(x_fit, a, b)

# Plot der Daten und des Fits
plt.scatter(x, y, label='Daten')
plt.plot(x_fit, y_fit, label='Fit: $y(x) = \\frac{1}{%.2f + %.2f \cdot x^2}$' % (a, b), color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Ausgabe der Parameter und des Fehlerfunktionals
print(f"Parameter a: {a}")
print(f"Parameter b: {b}")
print(f"Fehlerfunktional E: {E}")
