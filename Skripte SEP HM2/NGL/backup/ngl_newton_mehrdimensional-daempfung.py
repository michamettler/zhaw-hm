import numpy as np
import sympy as sp

# Funktion und Jacobi-Matrix symbolisch erzeugen
x1, x2 = sp.symbols('x1, x2')
x = sp.Matrix([x1, x2])
print(x)
# Matrix([[x1],
#         [x2]])

f1 = x1**2 + x2 - 11
f2 = x1 + x2**2 - 7
f = sp.Matrix([f1, f2])
print(f)
# Matrix([[x1**2 + x2 - 11],
#         [x1 + x2**2 - 7]])

Df = f.jacobian(x)
print(Df)
# Matrix([[2*x1, 1],
#         [1, 2*x2]])

# Funktion und Jacobi-Matrix numerisch umwandeln
f = sp.lambdify([[x1, x2]], f, 'numpy')
Df = sp.lambdify([[x1, x2]], Df, 'numpy')
print(f)  # <function _lambdifygenerated at 0x0000016D4CB4C700>
print(Df)  # <function _lambdifygenerated at 0x0000016D4CB4C1F0>

# Funktion und Jacobi-Matrix numerisch auswerten
x = np.array([1., 1.])
print(f(x))  # Gibt Funktionswert als 2D-Array aus!
# [[-9.]
#  [-5.]]
print(f(x).flatten())  # Wandelt Funktionswert in 1D-Array um
# [-9. -5.]

print(Df(x))
# [[2. 1.]
#  [1. 2.]]

# Newtonverfahren mit Daempfung numerisch durchfuehren
i = 0
x = np.array([1., 1.])
print('i =', i, ', x =', x, ', ||f(x)|| =', np.linalg.norm(f(x), 2))

imax = 5
for i in range(1, imax + 1):
    delta = np.linalg.solve(Df(x), -f(x).flatten())
    # Umwandlung von f(x0) in 1D-Array ergibt delta0 als 1D-Array

    # Daempfung
    kmax = 4  # maximale Anzahl Daempfungsschritte
    k = 0
    while (k <= kmax) and (np.linalg.norm(f(x + delta / 2**k), 2) >= np.linalg.norm(f(x), 2)):
        k = k + 1
    if k == kmax + 1:
        k = 0

    x = x + delta / 2**k
    print('i =', i, ', k =', k, ', x =', x, ', ||f(x)|| =', np.linalg.norm(f(x), 2))

# Ausgabe:
# i = 0 x = [1. 1. ] ||f(x)|| = 10.295630140987
# i = 1 k = 1 x = [3.16666667 1.16666667] ||f(x)|| = 2.479857124518405
# i = 2 k = 0 x = [2.9543018  2.3172043 ] ||f(x)|| = 1.324504879599893
# i = 3 k = 0 x = [2.99655306 2.02245497] ||f(x)|| = 0.086895508588128
# i = 4 k = 0 x = [2.99998037 2.00012951] ||f(x)|| = 0.0004985645907716054
# i = 5 k = 0 x = [3. 2.] ||f(x)|| = 1.677591381591778e-08