import sympy as sp
import numpy as np

x, y, z = sp.symbols('x, y, z')
A = sp.Matrix([x, y, z])

f1 = x*sp.exp(y) + z - 10
f2 = x*sp.exp(2*y) + 2*z - 12
f3 = x*sp.exp(3*y) + 3*z - 15
f = sp.Matrix([f1, f2, f3])
Df = f.jacobian(A)

f = sp.lambdify([[x, y, z]], f, 'numpy')
Df = sp.lambdify([[x, y, z]], Df, 'numpy')

x = np.array([1., 0.1, 2.])

i = 1
tol = 1e-5
while np.linalg.norm(f(x), 2) >= tol:
    delta = np.linalg.solve(Df(x), -f(x).flatten())
    
    kmax = 4 # max number of iterations
    k = 0
    while (k <= kmax) and (np.linalg.norm(f(x + delta / 2**k), 2) >= np.linalg.norm(f(x), 2)):
        k = k + 1
    if (k == kmax + 1):
        k = 0
    
    x = x + delta / 2**k
    print('i =', i, 'x =', x, '||f(x)|| =', np.linalg.norm(f(x), 2))
    i += 1
    