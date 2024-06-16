import numpy as np
import matplotlib.pyplot as plt

# INPUT

def f(x, y):
    return 0.1*y + np.sin(2*x)

def y_exact(x):
    return np.sqrt(x**2-3)

y0 = 0.
a = 0.
b = 6.
h = 0.2
n = int((b-a)/h)
print("n = ", n)

# --------------------------------------------------------------------


def R4_klassisch(f, a, b, n, y0):
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i]+h/2, y[i]+h/2*k1)
        k3 = f(x[i]+h/2, y[i]+h/2*k2)
        k4 = f(x[i]+h, y[i]+h*k3)
        k = 1/6*(k1+2*k2+2*k3+k4)
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*k
    return x, y

x, y_klassisch = R4_klassisch(f, a, b, n, y0)

"""
plt.figure(1)
plt.plot(x, y_klassisch, color="blue", linestyle="--", label="Lösung mit klassischem R4")
plt.plot(x, y_exact(x), color="purple", linestyle=":", label="Exakte Lösung")
plt.legend()
plt.show()
"""

def euler(f, a, y0, b, h):
    """
    Loest DGL y' = f(x, y) zum AW y(a) = y0 mit Euler-Verfahren
    auf Intervall [a, b] mit Schrittweite h
    Gibt die numerischen Naeherungswerte (x0, y0), (x1, y1), ..., (xn, yn)
    der exakten Loesung y(x) in zwei 1D-Arrays xnum = [x0, ..., xn] und ynum = [y0, ..., yn] zurueck
    """
    n = int((b - a) / h)
    xnum = np.zeros(n+1); xnum[0] = a
    ynum = np.zeros(n+1); ynum[0] = y0
    for i in range(n):
        xnum[i+1] = xnum[i] + h
        ynum[i+1] = ynum[i] + h * f(xnum[i], ynum[i])
    return xnum, ynum
"""


# Eigenes Butcher-Tableau
# 0.25 |
# 0.5  | 0.5
# 0.5  | 0.5 0.5
# 0.75 | 0.75 0.75 0.75
# --------------
#      | 0.1 0.4 0.4 0.1

def RK4_eigen(f, a, b, n, y0):
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    # Achtung: Umbenennung von a und b fuer eigene Koeffizienten
    c = np.array([0.25, 0.5, 0.5, 0.75])
    a = np.array([[0., 0., 0.],
                  [0.5, 0., 0.],
                  [0.5, 0.5, 0.],
                  [0.75, 0.75, 0.75]])
    b = np.array([0.1, 0.4, 0.4, 0.1])
    for i in range(n):
        k1 = f(x[i] + c[0]*h, y[i])
        k2 = f(x[i] + c[1]*h, y[i] + h* a[1,0]*k1)
        k3 = f(x[i] + c[2]*h, y[i] + h*(a[2,0]*k1 + a[2,1]*k2))
        k4 = f(x[i] + c[3]*h, y[i] + h*(a[3,0]*k1 + a[3,1]*k2 + a[3,2]*k3))
        k = b[0]*k1 + b[1]*k2 + b[2]*k3 + b[3]*k4
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*k
    return x, y
"""

# PLOTTEN und Fehler
x, y_eigen = R4_klassisch(f, a, b, n, y0)
x_euler, y_euler = euler(f, a, y0, b, h)
plt.figure(2)

plt.plot(x, y_eigen, color="red", linestyle="-", label="Lösung mit eigenem R4")
plt.plot(x, y_euler, color="blue", linestyle="--", label="Lösung mit klassischem R4")
#plt.plot(x, y_exact(x), color="purple", linestyle=":", label="Exakte Lösung")
plt.xlabel("x"); plt.ylabel("y"); plt.grid()
plt.legend()
plt.show()

plt.figure(3)
plt.semilogy(x, np.abs(y_eigen-y_euler), color="red", linestyle="-", label="absoluter Fehler mit eigenem R4")
plt.xlabel("x"); plt.grid()
plt.legend()
plt.show()