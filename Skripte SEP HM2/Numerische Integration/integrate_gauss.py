import numpy as np

# SUMMIERTE GAUSS-FORMEL

# Implementation
def sum_gauss(f, a, b, h):
    n = int((b - a) / h)
    G = 0
    alpha = 1 / 3**0.5 * 0.5
    for i in range(0, n):
        xm = a + i * h + h / 2  # mittlerer x-Wert des i-ten Teilintervalls
        G = G + f(xm - alpha * h / 2) + f(xm + alpha * h / 2)
    G = G / 2 * h
    return G

# INPUT
def f(x):
    return 1. / x

a = 2.
b = 4.
I = np.log(2.)
print(I)  # 0.6931471805599453

# Kontrolle mit h = 1
G = sum_gauss(f, a, b, 1.)
print(G)  # 0.693076382821177

# Fehler fuer h = 1, 0.1, 0.01, ...
kmax = 5
for k in range(0, kmax+1):
    h = 10.**(-k)
    G = sum_gauss(f, a, b, h)
    print(h, G, np.abs(G - I))

# Output format:
# h       G(h)                    |G(h) - I| (absolute error)
# 1.0     0.693076382821177       7.05422778274552e-05
# 0.1     0.6931471724354499      8.124495409767007e-09
# 0.01    0.6931471805591316      8.136824547477772
