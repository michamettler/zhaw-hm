import numpy as np

# ZWEISTUFIGE ROMBERG-EXTRAPOLATION

# Summierte Trapezregel
def sum_trapez(f, a, b, h):
    n = int((b - a) / h)
    T = (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * h
        T = T + f(x)
    T = h * T
    return T

# Zweistufige Romberg-Extrapolation der Trapezregel
def romberg_zweistufig(f, a, b, h):
    T00 = sum_trapez(f, a, b, h)
    T10 = sum_trapez(f, a, b, h / 2.)
    T20 = sum_trapez(f, a, b, h / 4.)
    T01 = (4 * T10 - T00) / 3.
    T11 = (4 * T20 - T10) / 3.
    T02 = (16 * T11 - T01) / 15.
    return T02

# Beispiel
def f(x):
    return 1. / x

a = 2.
b = 4.
I = np.log(2.)
print('I =', I)  # I = 0.6931471805599453

# Kontrolle mit h = 2
E = romberg_zweistufig(f, a, b, 2.)
print('E =', E)  # E = 0.6931746031746032

# Fehler fuer h = 1, 0.1, 0.01, ...
kmax = 5
for k in range(0, kmax + 1):
    h = 10.**(-k)
    E = romberg_zweistufig(f, a, b, h)
    print(h, E, np.abs(E - I))

# Output format:
# h       E(h)                    |E(h) - I| (absolute error)
# 1.0     0.6931479014812348      7.209212895542549e-07
# 0.1     0.6931471805608955      9.502398867766715e-13
# 0.01    0.693147180559945       3.3306690738754696e-16
# 0.001   0.6931471805599448      4.440892098500626e-16
# 0.0001  0.6931471805599286      1.6653345369377348e-14
# 0.00001 0.6931467916710429      3.88888902413953e-07
