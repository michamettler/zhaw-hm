import numpy as np

# Klassisches vierstufiges Runge-Kutta-Verfahren
def rk4_klassisch(f, a, y0, b, h):
    """
    Loest DGL y' = f(x, y) zum AW y(a) = y0 mit klassischem vierstufigem
    Runge-Kutta-Verfahren auf Intervall [a, b] mit Schrittweite h
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
        k3 = h * f(xnum[i] + h / 2, ynum[i] + k2 / 2)
        k4 = h * f(xnum[i] + h, ynum[i] + k3)
        ynum[i + 1] = ynum[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return xnum, ynum

# Beispiel
def f(x, y): return y - x**2

a = 0.; y0 = 1; b = 2
def yexakt(x): return -np.exp(x) + x**2 + 2*x + 2

# Schrittweite h = 1
h = 1
xnum, ynum = rk4_klassisch(f, a, y0, b, h)
print(xnum)
print(ynum)
# [0.  1.  2. ]
# [1.         2.27083333 2.58767361]

# Genauigkeit des Endwerts yn
# in Abhaengigkeit der Schrittweite h = 0.1, 0.01, 0.001, ...
yb = yexakt(b)  # exakter Endwert
print(yb)  # 2.6109439010693496
for k in range(6):
    h = 10**-k
    xnum, ynum = rk4_klassisch(f, a, y0, b, h)
    print(h, ynum[-1], np.abs(ynum[-1] - yb))

# Ausgabeformat:
# h       yn                      |yn - y(b)|
# 0.1     2.61094276553958        1.3245297694197689e-06
# 0.01    2.61094389962196        1.031299490250634e-10
# 0.001   2.6109439010695805      2.3092638912203256e-13
# 0.0001  2.610943901069278       3.0890960736678027e-13
# 0.00001 2.6109439010690277      9.28146448566309e-13
# 0.000001 2.610943901035691      1.3890287555717826e-05
