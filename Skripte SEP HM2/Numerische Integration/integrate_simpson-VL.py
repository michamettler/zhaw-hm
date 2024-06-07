import numpy as np

# SUMMIERTE SIMPSONREGEL

# Implementation
def sum_simpson(f, a, b, h):
    n = int((b - a) / h)
    S = f(a) + f(b) + 4 * f(a + h / 2)
    for i in range(1, n):
        x = a + i * h
        S = S + 2 * f(x) + 4 * f(x + h / 2)
    S = h / 6 * S
    return S

# Beispiel
def f(x):
    return 1. / x

a = 2.
b = 4.
I = np.log(2.)
print(I)  # 0.6931471805599453

# Kontrolle mit h = 1
S = sum_simpson(f, a, b, 1.)
print(S)  # 0.6932539682539682

# Fehler fuer h = 1, 0.1, 0.01, ...
kmax = 5
for k in range(0, kmax+1):
    h = 10.**(-k)
    S = sum_simpson(f, a, b, h)
    print(h, S, np.abs(S - I))

# Output format:
# h       S(h)                    |S(h) - I| (absolute error)
# 1.0     0.6932539682539682      0.0001067876940229473
# 0.1     0.693147192747956       1.218801071788877e-08
# 0.01    0.693147180561166       1.220692155753596e-12
# 0.001   0.6931471805599476      2.3314683517128287e-15
# 0.0001  0.6931471805599437      1.5543122344752192e-15
# 0.00001 0.6931446805558094      2.5000041359302116e-09
