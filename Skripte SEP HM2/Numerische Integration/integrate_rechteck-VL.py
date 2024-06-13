import numpy as np

# SUMMIERTE TRAPEZREGEL

# Implementation
def sum_trapez(f, a, b, h):
    n = int((b - a) / h)
    T = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        T = T + f(x)
    T = h * T
    return T

# Beispiel
def f(x):
    return 1. / x

a = 2.
b = 4.
I = np.log(2.)
print(I)  # 0.6931471805599453

# Kontrolle mit h = 0.5
T = sum_trapez(f, a, b, 0.5)
print(T)  # 0.6970238095238095

# Fehler fuer h = 1, 0.1, 0.01, ...
kmax = 5
for k in range(0, kmax+1):
    h = 10.**(-k)
    T = sum_trapez(f, a, b, h)
    print(h, T, np.abs(T - I))

# Output format:
# h       T(h)                    |T(h) - I| (absolute error)
# 1.0     0.7083333333333333      0.015186152773387973
# 0.1     0.69303881792694        0.00015620123274873166
# 0.01    0.69314734050624        1.562495170689627e-06
# 0.001   0.6931471961849452      1.562499996055067e-08
# 0.0001  0.69314718091785        3.57904384247327e-10
# 0.00001 0.6931471805595238      2.500048683787878e-12
