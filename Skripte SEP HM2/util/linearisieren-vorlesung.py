
import sympy as sp

# Variablen festlegen
x1, x2, x3 = sp.symbols('x1, x2, x3')
x = sp.Matrix([x1, x2, x3])
print(x)
# Matrix([[x1], [x2], [x3]])

# Funktionen festlegen
f1 = x1*sp.cos(x2) + x3
f2 = x1**2 + sp.sin(x2)*x3**3
f = sp.Matrix([f1, f2])
print(f)
# Matrix([[x1*cos(x2) + x3], [x1**2 + x3**3*sin(x2)]])

# Jacobi-Matrix bilden
Df = f.jacobian(x)
print(Df)
# Matrix([[cos(x2), -x1*sin(x2), 1], [2*x1, x3**3*cos(x2), 3*x3**2*sin(x2)]])

# Stelle festlegen
x0 = sp.Matrix([1, 0, -1])
print(x0)
# Matrix([[1], [0], [-1]])

# Funktionen und Jacobi-Matrix an Stelle auswerten
fx0 = f.subs([(x1, x0[0,0]), (x2, x0[1,0]), (x3, x0[2,0])])
print(fx0)
# Matrix([[0], [1]])

Dfx0 = Df.subs([(x1, x0[0,0]), (x2, x0[1,0]), (x3, x0[2,0])])
print(Dfx0)
# Matrix([[1, 0, 1], [2, -1, 0]])

# Linearisierung von Funktionen an Stelle bilden
g = fx0 + Dfx0 @ (x - x0)
print(g)
# Matrix([[x1 + x3], [2*x1 - x2 - 1]])
