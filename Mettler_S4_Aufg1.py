# Hoehere Mathematik 1 - Serie 4 Aufgabe 1 Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt

# 4a

def fixpunktiteration(f, x0, n):
    x = np.zeros(n+1)
    x[0] = x0
    for i in range (1, n+1):
        x[i] = f(x[i-1])
    return x

def F(x):
    return (230*x**4 + 18*x**3 + 9*x**2 - 9)/221

def df(x):
    return (4*230*x**3 + 3*18*x**2 + 2*9*x)/221

x1 = fixpunktiteration(F, 0, 4)
print('x1', x1)
x2 = fixpunktiteration(F, 1, 4)
print('x2', x2)

# 4b

x = np.arange(-0.5, 0.5, .01)
plt.plot(x, F(x))
plt.xlabel('x')
plt.ylabel('y')
plt.title('F(x)')
plt.grid()
print("max Steigung: {}".format(df(.5)))

# 4c 39 Mal - nein ist nicht nötig