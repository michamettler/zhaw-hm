# Hoehere Mathematik 1 - Serie 5 Aufgabe 3 Micha Mettler (mettlmi1)

# Imports
import numpy as np


def Mettler_S5_Aufg3(f, x0, x1, tol):
    while f(x1 - tol) * f(x1 + tol) >=0:
        temp = x1
        x1 = x1 - (x1 - x0) / (f(x1) - f(x0)) * f(x1)
        x0 = temp
    return x1


def f(x):
    return np.exp(x**2)+ x**-3 - 10

res = Mettler_S5_Aufg3(f, -1, -1.2, 1e-5)
print(res)
