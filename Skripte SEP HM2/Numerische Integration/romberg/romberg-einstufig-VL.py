import numpy as np

# EINSTUFIGE ROMBERG-EXTRAPOLATION

# Summierte Trapezregel
def sum_trapez(f, a, b, h):
    n = int((b - a) / h)
    T = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        T = T + f(x)
    T = h * T
    return T

# Einstufige Romberg-Extrapolation der Trapezregel
def romberg_einstufig(f, a, b, h):
    E = (4. * sum_trapez(f, a, b, h / 2.) - sum_trapez(f, a, b, h)) / 3.
    return E

# Beispiel
def f(x):
    return 1. / x

a = 2.
b = 4.
I = np.log(2.)
print(I)  # 0.6931471805599453

# Kontrolle mit h = 2
E = romberg_einstufig(f, a, b, 2.)
print(E)  # 0.6944444444444443

# Fehler fuer h = 1, 0.1, 0.01, ...
kmax = 5
for k in range(0, kmax + 1):
    h = 10.**(-k)
    E = romberg_einstufig(f, a, b, h)
    print(h, E, np.abs(E - I))

# Output format:
# h       E(h)                    |E(h) - I| (absolute error)
# 1.0     0.6932539682539683      0.0001067876940205832
# 0.1     0.6931471927479563      1.2188011044855784e-08
# 0.01    0.6931471805611662      1.2209122601802846e-12
# 0.001   0.6931471805599457      4.440892098500626e-16
# 0.0001  0.6931471805599453      9.325873406851315e-15
# 0.00001 0.6931463472266192      8.33333326122343e-07
