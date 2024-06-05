import numpy as np

# Funktion f: R^2 -> R^2, x = [x1, x2] -> f(x) = [f1(x1, x2), f2(x1, x2)]
def f(x):
    f1 = x[0]**2 + x[1] - 11
    f2 = x[0] + x[1]**2 - 7
    return np.array([f1, f2])

# Jacobi-Matrix Df = [[df1dx1, df1dx2], [df2dx1, df2dx2]] von f
def Df(x):
    df1dx1 = 2.*x[0]
    df1dx2 = 1.
    df2dx1 = 1.
    df2dx2 = 2.*x[1]
    return np.array([[df1dx1, df1dx2], [df2dx1, df2dx2]])

# Nullstelle von f
xstar = np.array([3., 2.])

# VEREINFACHTES NEWTON-VERFAHREN MIT STARTWERT x = (1, 1)
x = np.array([1., 1.])
D = Df(x)
imax = 3
for i in range(1, imax + 1):
    delta = np.linalg.solve(D, -f(x))
    x = x + delta
    error = np.linalg.norm(x - xstar, 2)
    print('i =', i, ', x =', x, ', ||x - xstar|| =', error)

# i = 1 x = [5.33333333 1.33333333] ||x - xstar|| = 2.426703296426839
# i = 2 x = [-7.14814815 7.51851852] ||x - xstar|| = 11.55157813789936
# i = 3 x = [-24.7645176  -4.86328304] ||x - xstar|| = 28.60022887702252

# Das vereinfachte Newton-Verfahren divergiert. Der Startwert liegt nicht nahe genug bei der Nullstelle.

# VEREINFACHTES NEWTON-VERFAHREN MIT STARTWERT x = (2.5, 1.5)
x = np.array([2.5, 1.5])
D = Df(x)
imax = 3
for i in range(1, imax + 1):
    delta = np.linalg.solve(D, -f(x))
    x = x + delta
    error = np.linalg.norm(x - xstar, 2)
    print('i =', i, ', x =', x, ', ||x - xstar|| =', error)

# i = 1 x = [3.03571429 2.07142857] ||x - xstar|| = 0.0798595706249922
# i = 2 x = [2.99754009 1.97530977] ||x - xstar|| = 0.02481247406886527
# i = 3 x = [2.99880578 2.00842495] ||x - xstar|| = 0.008509165487905259

# Das vereinfachte Newton-Verfahren konvergiert. Es gilt näherungsweise
# Fehler nach Schritt i+1 = 1/3 * Fehler nach Schritt i.

# Das vereinfachte Newton-Verfahren hat KONVERGENZORDNUNG 1,
# d.h. es konvergiert LINEAR.
