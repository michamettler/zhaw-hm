import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Gegebene Punkte
x = np.array([0, 2, 6])
y = np.array([0.1, 0.9, 0.1])

# Kubische Spline-Interpolation mit natürlichen Randbedingungen
cs = CubicSpline(x, y, bc_type='natural')

# Erstellen eines feinen Gitters zum Plotten der Spline-Funktion
x_fine = np.linspace(0, 6, 100)
y_fine = cs(x_fine)

# Plotten der Punkte und der interpolierten Spline
plt.figure(figsize=(8, 4))
plt.plot(x, y, 'o', label='Gegebene Punkte')
plt.plot(x_fine, y_fine, '-', label='Kubische Spline-Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Kubische Spline-Interpolation der Coins')
plt.legend()
plt.grid(True)
plt.show()
