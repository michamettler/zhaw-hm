import numpy as np

# Modifiziertes Euler-Verfahren
def euler_modifiziert(f, a, y0, b, h):
    """
    Loest DGL y' = f(x, y) zum AW y(a) = y0 mit modifiziertem Euler-Verfahren
    auf Intervall [a, b] mit Schrittweite h
    Gibt die numerischen Naeherungswerte (x0, y0), (x1, y1), ..., (xn, yn)
    der exakten Loesung y(x) in zwei 1D-Arrays xnum = [x0, ..., xn] und ynum = [y0, ..., yn] zurueck
    """
    n = int((b - a) / h)
    xnum = np.zeros(n + 1); xnum[0] = a
    ynum = np.zeros(n + 1); ynum[0] = y0
    for i in range(n):
        xnum[i + 1] = xnum[i] + h
        k1 = h * f(xnum[i], ynum[i])
        k2 = h * f(xnum[i] + h, ynum[i] + k1)
        ynum[i + 1] = ynum[i] + 0.5 * (k1 + k2)
    return xnum, ynum

# Beispiel
def f(x, y): return y - x**2

a = 0.; y0 = 1; b = 2
def yexakt(x): return -np.exp(x) + x**2 + 2*x + 2

# Schrittweite h = 0.5
h = 0.5
xnum, ynum = euler_modifiziert(f, a, y0, b, h)
print(xnum)
print(ynum)
# [0.  0.5 1.  1.5 2. ]
# [1.        1.5625    2.1953125 2.62988281 2.42980957]

# Genauigkeit des Endwerts yn
# in Abhaengigkeit der Schrittweite h = 0.1, 0.01, 0.001, ...
yb = yexakt(b)  # exakter Endwert
print(yb)  # 2.6109439010693496
for k in range(5):
    h = 10**-k
    xnum, ynum = euler_modifiziert(f, a, y0, b, h)
    print(h, ynum[-1], np.abs(ynum[-1] - yb))

# Ausgabeformat:
# h       yn                      |yn - y(b)|
# 0.1     2.603449754065215       0.007494147004134533
# 0.01    2.610870507694765       7.339337458311945e-05
# 0.001   2.610936583701909       7.317583607525986e-07
# 0.0001  2.610943897458222       3.6111233479362e-09
# 0.00001 2.610943901069349       7.31445704052957e-09
