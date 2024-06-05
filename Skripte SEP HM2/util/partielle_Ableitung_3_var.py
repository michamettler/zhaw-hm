# Modul fuer symbolische Berechnungen importieren
import sympy as sp

# Symbolische Variablen einfuehren
x1, x2, x3 = sp.symbols('x1, x2, x3')

# Symbolische Variablen zu symbolischem Vektor in Form von symbolischer Spaltenmatrix zusammenfassen
x = sp.Matrix([x1, x2, x3])
print(x)
# Matrix([[x1],
#         [x2],
#         [x3]])

# Skalare symbolische Terme erzeugen
f1 = x1*sp.cos(x2) + x3
f2 = x1**2 + sp.sin(x2)*x3**3

# Skalare symbolische Terme zu vektoriellen symbolischem Term in Form von symbolischer Spaltenmatrix zusammenfassen
f = sp.Matrix([f1, f2])
print(f)
# Matrix([[x1*cos(x2) + x3],
#         [x1**2 + x3**3*sin(x2)]])

# Symbolische Jacobi-Matrix bilden
Df = f.jacobian(x)
print(Df)
# Matrix([[cos(x2), -x1*sin(x2), 1],
#         [2*x1, x3**3*cos(x2), 3*x3**2*sin(x2)]])