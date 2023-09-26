# Höhere Mathematik 1 - Serie 1 Aufgabe 1 Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Intervall [-4, 4]
x = np.arange(-4, 4, 0.01)

# Polynom x^3 + 2x^2 - 3x - 4
def f(x):
    return x**3 + 2 * x**2 - 3 * x - 4.

# Ableitungsfunktion von Polynom x^3 + 2x^2 - 3x - 4
def df(x):
    return 3. * x ** 2 + 4 * x - 3

# Stammfunktion von Polynom x^3 + 2x^2 - 3x - 4
def F(x):
    return 1/4. * x**4 + 2/3. * x**3 - 3/2. * x**2 - 4 * x

# Plotten
plt.ylim(-10., 10.)
plt.grid()
plt.plot(x, f(x))
plt.plot(x, df(x))
plt.plot(x, F(x))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)', 'df(x)', 'F(x)'])
plt.title('Plot von Polynom, Ableitung und Stammfunktion')