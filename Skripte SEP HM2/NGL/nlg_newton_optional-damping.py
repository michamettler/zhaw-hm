import sympy as sp
import numpy as np

# SymPy Symbole und Matrixdefinition
x, y = sp.symbols('x, y')
A = sp.Matrix([x, y])

# Definition der Funktionen
f1 = x**2 + y-11
f2 = x + y**2 - 7
f = sp.Matrix([f1, f2])
Df = f.jacobian(A)

# Konvertierung in numpy-fähige Funktionen
f = sp.lambdify([[x, y]], f, 'numpy')
Df = sp.lambdify([[x, y]], Df, 'numpy')

# Anfangswerte
x = np.array([1., 1.])

# Parameter
i = 1
tol = 1e-4
damping = True  # Dämpfung ein-/ausschalten

# Iteration
while np.linalg.norm(f(x), 2) >= tol:
    delta = np.linalg.solve(Df(x), -f(x).flatten())
    
    if damping:
        # Dämpfung aktivieren
        kmax = 19  # max number of iterations
        k = 0
        while (k <= kmax) and (np.linalg.norm(f(x + delta / 2**k), 2) >= np.linalg.norm(f(x), 2)):
            k = k + 1
        if (k == kmax + 1):
            k = 0
        x = x + delta / 2**k
    else:
        # Dämpfung deaktivieren
        x = x + delta
    
    print('i =', i, 'x =', x, '||f(x)|| =', np.linalg.norm(f(x), 2))
    i += 1
