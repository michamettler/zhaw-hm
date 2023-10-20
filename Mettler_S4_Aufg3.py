# Hoehere Mathematik 1 - Serie 4 Aufgabe 3 Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt

# 3a vgl. Praktikumsnotizen

# 3b

def F(phi):
    return np.sin(phi) + (1/2)*np.pi

def fixpunktiteration(f, x0, n):
    x = np.zeros(n+1)
    x[0] = x0
    for i in range (1, n+1):
        x[i] = f(x[i-1])
    return x

# Skizze (Plot)
x = np.arange(0, np.pi, .01)
plt.plot(x, F(x))
plt.xlabel('x')
plt.ylabel('y')

# Fixpunktiteration
print('Fixpunktiteration', fixpunktiteration(F, 2.3, 12))

# 3c ca. 1.404*r (Lösungen, Trigo nicht meine Stärke)