import numpy as np

# Mittelpunkt-Verfahren
def mittelpunkt(f, a, y0, b, h):
    """
    Loest DGL y' = f(x, y) zum AW y(a) = y0 mit Mittelpunkt-Verfahren
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
        k2 = h * f(xnum[i] + h / 2, ynum[i] + k1 / 2)
        ynum[i + 1] = ynum[i] + k2
    return xnum, ynum

# Beispiel
def f(x, y): return y - x**2

a = 0.; y0 = 1; b = 2
def yexakt(x): return -np.exp(x) + x**2 + 2*x + 2

# Schrittweite h = 0.5
h = 0.5
xnum, ynum = mittelpunkt(f, a, y0, b, h)
print(xnum)
print(ynum)
# [0.  0.5 1.  1.5 2. ]
# [1.         1.59375    2.27734375 2.79443359 2.72845459]

# Genauigkeit des Endwerts yn
# in Abhaengigkeit der Schrittweite h = 0.1, 0.01, 0.001, ...
yb = yexakt(b)  # exakter Endwert
print(yb)  # 2.6109439010693496
for k in range(6):
    h = 10**-k
    xnum, ynum = mittelpunkt(f, a, y0, b, h)
    print(h, ynum[-1], np.abs(ynum[-1] - yb))

# Ausgabeformat:
# h       yn                      |yn - y(b)|
# 0.1     2.6180674566067983      0.00766355500448685
# 0.01    2.61102943353748        0.000085322813035219
# 0.001   2.6109447657716993      8.647068496792087e-07
# 0.0001  2.610943902767138       1.6986735483892733e-09
# 0.00001 2.610957191443357       1.3890374026104269e-05
