import numpy as np

# Euler-Verfahren
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

# INPUT
def f(x, y): return y - x**2

a = 0.; y0 = 1; b = 2
def yexakt(x): return -np.exp(x) + x**2 + 2*x + 2

# Schrittweite h = 0.5
h = 0.5
xnum, ynum = euler(f, a, y0, b, h)
print(xnum)
print(ynum)
# [0.  0.5 1.  1.5 2. ]
# [1.     1.5    2.125  2.6875 2.90625]

# Genauigkeit des Endwerts yn
# in Abhaengigkeit der Schrittweite h = 0.1, 0.01, 0.001, ...
yb = yexakt(b)  # exakter Endwert
print(yb)  # 2.6109439010693496
for k in range(5):
    h = 10**-k
    xnum, ynum = euler(f, a, y0, b, h)
    print(h, ynum[-1], np.abs(ynum[-1] - yb))

# Ausgabeformat:
# h       yn                      |yn - y(b)|
# 0.1     2.69975055714388        0.08880615467248854
# 0.01    2.6208219756577556      0.00987806858240603
# 0.001   2.6119427969405418      0.0009988958711917172
# 0.0001  2.61104843565356        0.00010453458421086847
# 0.00001 2.6109439014363556      3.668078318230355e-10
