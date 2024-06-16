import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Eingabewerte
x = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0], dtype=np.float64)
y = np.array([39.55, 46.55, 50.13, 51.75, 55.25, 56.79, 56.78, 59.13, 57.76, 59.39, 60.08], dtype=np.float64)

# Plot der Datenpunkte
plt.plot(x, y, 'o', label='Datenpunkte')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Datenpunkte ohne Anfangswerte')
plt.legend()
plt.show()

# => Ablesen der Startwerte

lam0 = np.array([30, 70, 0.2], dtype=np.float64)
tol = 1e-7

p0, p1, p2 = sp.symbols('p0 p1 p2')
p = [p0, p1, p2]

def f(x, p):
    return p[0] + (p[1] - p[0]) * (1 - sp.exp(-p[2] * x / sp.pi))

# --------------------------------------------------------

g = sp.Matrix([y[k] - f(x[k], p) for k in range(len(x))])
Dg = g.jacobian(p)

g_lambdified = sp.lambdify([p], g, 'numpy')
Dg_lambdified = sp.lambdify([p], Dg, 'numpy')

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

# Ohne Dämpfung
def gauss_newton(g, Dg, lam0, tol, max_iter):
    k = 0
    lam = np.copy(lam0)
    increment = tol + 1
    err_func = np.linalg.norm(g(lam))**2

    while increment >= tol and k <= max_iter:
        # QR-Zerlegung von Dg(lam) und delta als Lösung des lin. Gleichungssystems
        Q, R = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()

        # Update des Vektors Lambda        
        lam = lam + delta
        err_func = np.linalg.norm(g(lam))**2
        increment = np.linalg.norm(delta)
        k += 1
        print('Iteration: ', k)
        print('lambda = ', lam)
        print('Inkrement = ', increment)
        print('Fehlerfunktional =', err_func)
    return lam, k

# Mit Dämpfung
def gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping):
    k = 0
    lam = np.copy(lam0)
    increment = tol + 1
    err_func = np.linalg.norm(g(lam))**2

    while increment >= tol and k < max_iter:
        # QR-Zerlegung von Dg(lam)
        Q, R = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()
        
        # Dämpfung
        p = 0
        if damping:
            while p < pmax and np.linalg.norm(g(lam + delta / 2**p))**2 >= err_func:
                p += 1
            if p == pmax + 1:
                p = 0

        # Update des Vektors Lambda        
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
lam_without, n = gauss_newton(g_lambdified, Dg_lambdified, lam0, tol, max_iter)

# Mit Dämpfung
max_iter = 30
pmax = 5  # maximale Dämpfung
damping = 1  # Dämpfung aktivieren
lam_with, n = gauss_newton_d(g_lambdified, Dg_lambdified, lam0, tol, max_iter, pmax, damping)

t = sp.symbols('t')
F = f(t, lam_without)
F = sp.lambdify(t, F, 'numpy')
t_vals = np.arange(0, 3, 0.001) # Intervall für die Interpolation

plt.plot(x, y, 'o')
plt.plot(t_vals, F(t_vals))
plt.xlabel('x')
plt.ylabel('y')
plt.show()
