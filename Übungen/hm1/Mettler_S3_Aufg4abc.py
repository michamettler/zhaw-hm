# Hoehere Mathematik 1 - Serie 3 Aufgabe 4a und 4b Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt

# 4a
x = np.arange(1.1, 1.3, 1e-7)

def h(x):
    return np.sqrt(100*x**2 - 200*x + 99)

plt.figure(1)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, h(x))
plt.ylabel('f(x)')
plt.grid()

# Erklärung, siehe Plot (Wert in Richtung 0)

# 4b

def dh(x):
    return 100*(1-x)/h(x)
def K(x):
    return np.abs(x*dh(x)/h(x))

plt.figure(2)
plt.semilogy(x, K(x))
plt.xlabel('x')
plt.ylabel('y')
plt.ylabel('K(x)')
plt.grid()

# Auslöschung nicht vermeiden da gegen Unendlich

