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

# Newton-Verfahren
x = np.array([1., 1.])  # Startwert
imax = 5  # Anzahl Iterationsschritte
for i in range(1, imax + 1):
    x = x - np.linalg.inv(Df(x)) @ f(x)  # Newton-Iterationsschritt
    error = np.linalg.norm(x - xstar, 2)  # absoluter Fehler bez. 2-Norm
    print('i =', i, ', x =', x, ', ||x - xstar|| =', error)

# i = 1 x = [5.33333333 1.33333333] ||x - xstar|| = 2.4267032964268402
# i = 2 x = [3.51282051 1.97435897] ||x - xstar|| = 0.5134611383205334
# i = 3 x = [3.03880731 1.99038687] ||x - xstar|| = 0.03999185164582465
# i = 4 x = [3.00002545 1.99995953] ||x - xstar|| = 0.00025765409137650235
# i = 5 x = [3.00000001 2.        ] ||x - xstar|| = 1.1440143329366726e-08

# Konvergenz
# Nach dem 2. Iterationsschritt ist der Fehler von der Größenordnung 10^-1
# nach dem 3. Iterationsschritt ist der Fehler von der Größenordnung 10^-2
# nach dem 4. Iterationsschritt ist der Fehler von der Größenordnung 10^-4
# nach dem 5. Iterationsschritt ist der Fehler von der Größenordnung 10^-8

# Es gilt also größenordnungsmäßig
# Fehler nach Schritt i+1 = (Fehler nach Schritt i)^2

# Das Newton-Verfahren hat KONVERGENZORDNUNG 2 bzw. konvergiert QUADRATISCH.
