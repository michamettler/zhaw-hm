# Hoehere Mathematik 1 - Serie 2 Aufgabe 1a Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt

steps = (2.01-1.99)/501
x = np.arange(1.99, 2.01, steps)

def f1(x):
    return x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128

def f2(x):
    return (x - 2)**7


# Plotten
plt.grid()
plt.plot(x, f1(x))
plt.plot(x, f2(x))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f1(x)', 'f2(x)'])
plt.title('Vergleich Ausmultiplizieren')

# Erklärung a)
# Letzte Subtraktion (-128) zu gross (Kommentar in VL dass Subtraktionen gefährlich werden können)