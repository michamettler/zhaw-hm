import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Eingabewerte
x_vals = np.array([0., 2., 4., 6., 8., 10.], dtype=np.float64)
y_vals = np.array([52.9, 184., 426., 529., 499., 510.], dtype=np.float64)

# Plot der Datenpunkte
plt.plot(x_vals, y_vals, 'o', label='Datenpunkte')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Datenpunkte ohne Anfangswerte')
plt.legend()
plt.show()

# Startwerte
lam0 = np.array([20., 450., 0.001], dtype=np.float64)
tol = 1e-7

# SymPy Symbole
p0, p1, p2 = sp.symbols('p0 p1 p2')
p = [p0, p1, p2]

# Definition der Funktion f(x, p)
def f(x, p):
    return p[1] / (1 + (p[1] / p[0] - 1) * sp.exp(-p[2] * p[1] * x))

# Definition der Fehlerfunktional
g = sp.Matrix([y_vals[k] - f(x_vals[k], p) for k in range(len(x_vals))])
Dg = g.jacobian(p)

# Lambdifizierte Funktionen
g_lambdified = sp.lambdify([p], g, 'numpy')
Dg_lambdified = sp.lambdify([p], Dg, 'numpy')

## ------------------ Initialisierung --------------------
k = 0
lam = np.copy(lam0)
Q, R = np.linalg.qr(Dg_lambdified(lam))
delta = np.linalg.solve(R, -Q.T @ g_lambdified(lam)).flatten()
lam = lam + delta
increment = np.linalg.norm(delta)

# Fehlerfunktional des Startvektors lam0
err_func0 = np.linalg.norm(g_lambdified(lam0))**2
# Fehlerfunktional nach der ersten Iteration
err_func = np.linalg.norm(g_lambdified(lam))**2

# Ausgabe der Initialisierungsergebnisse
print('Initialisierung:')
print('lambda = ', lam)
print('Inkrement = ', increment)
print('Fehlerfunktional =', err_func)
## ------------------------------------------------------


# Gauss-Newton ohne Dämpfung
def gauss_newton(g, Dg, lam0, tol, max_iter):
    k = 0
    lam = np.copy(lam0)
    increment = tol + 1
    err_func = np.linalg.norm(g(lam))**2

    while increment >= tol and k <= max_iter:
        Q, R = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()

        lam = lam + delta
        err_func = np.linalg.norm(g(lam))**2
        increment = np.linalg.norm(delta)
        k += 1
        print('Iteration: ', k)
        print('lambda = ', lam)
        print('Inkrement = ', increment)
        print('Fehlerfunktional =', err_func)
    return lam, k

# Gauss-Newton mit Dämpfung
def gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping):
    k = 0
    lam = np.copy(lam0)
    increment = tol + 1
    err_func = np.linalg.norm(g(lam))**2

    while increment >= tol and k < max_iter:
        Q, R = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()

        p = 0
        if damping:
            while p < pmax and np.linalg.norm(g(lam + delta / 2**p))**2 >= err_func:
                p += 1
            if p == pmax + 1:
                p = 0

        lam = lam + delta / 2**p
        err_func = np.linalg.norm(g(lam))**2
        increment = np.linalg.norm(delta / 2**p)
        k += 1
        print('Iteration: ', k)
        print('lambda = ', lam)
        print('Inkrement = ', increment)
        print('Fehlerfunktional =', err_func)
    return lam, k

# Final Input

# Ohne Dämpfung
max_iter = 30
#lam_without, n = gauss_newton(g_lambdified, Dg_lambdified, lam0, tol, max_iter)

# Mit Dämpfung
max_iter = 30
pmax = 5  # maximale Dämpfung
damping = 1  # Dämpfung aktivieren
lam_with, n = gauss_newton_d(g_lambdified, Dg_lambdified, lam0, tol, max_iter, pmax, damping)

# Interpolation
t = sp.symbols('t')
F = f(t, lam_with)
F = sp.lambdify(t, F, 'numpy')
t_vals = np.arange(0, 10, 0.001) # Intervall für die Interpolation

# Plot
plt.plot(x_vals, y_vals, 'o', label='Datenpunkte')
plt.plot(t_vals, F(t_vals), label='Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
