import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def f1(x, y):
    return x**2/186**2 - y**2/(300**2 - 186**2) - 1
def f2(x, y):
    return (y - 500)**2/279**2 - (x - 300)**2/(500**2 - 279**2) - 1

# Teilaufgabe a)
x = np.arange(-2000., 2000., 1.)
y = np.arange(-2000., 2000., 1.)
X1, X2 = np.meshgrid(x, y)
Y1 = f1(X1, X2)
Y2 = f2(X1, X2)

plt.contour(X1, X2, Y1, levels=[0], colors='r')
plt.contour(X1, X2, Y2, levels=[0], colors='b')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Lösungen: (-1300, 1600), (-200, 100), (300, 200), (700, 900)

# Teilaufgabe b)
x1, x2 = sp.symbols('x1, x2')
x = sp.Matrix([x1, x2])

f1 = x1**2/186**2 - x2**2/(300**2 - 186**2) - 1
f2 = (x2 - 500)**2/279**2 - (x1 - 300)**2/(500**2 - 279**2) - 1
f = sp.Matrix([f1, f2])
Df = f.jacobian(x)

f = sp.lambdify([[x1, x2]], f, 'numpy')
Df = sp.lambdify([[x1, x2]], Df, 'numpy')

def newton(f, Df, xn, tol):
    while np.linalg.norm(f(xn), 2) >= tol:
        delta = np.linalg.solve(Df(xn), -f(xn).flatten()) # flatten back to 1D array
        xn = xn + delta
    return xn

x = np.array([-1300., 1600.])
tol = 1e-5

x = newton(f, Df, x, tol)
print('1. Iteration: x =', x)

x = np.array([-200., 100.])
x = newton(f, Df, x, tol)
print('2. Iteration: x =', x)

x = np.array([300., 200.])
x = newton(f, Df, x, tol)
print('3. Iteration: x =', x)

x = np.array([700., 900.])
x = newton(f, Df, x, tol)
print('4. Iteration: x =', x)