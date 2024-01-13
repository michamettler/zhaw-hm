import sympy as sp

# Definiere die symbolischen Variablen
x = sp.symbols('x')

# Erstelle eine Matrix mit diesen Variablen
matrix = sp.Matrix([
    [x, 1, 0],
    [1, x, 2],
    [0, 2, x],
])

# Zeige die Matrix
print("Matrix:")
sp.pprint(matrix)

# Definiere das Eigenwert-Symbol (lambda)
lambda_symbol = sp.symbols('lambda')

# Berechne das charakteristische Polynom der Matrix
char_poly = matrix.charpoly(lambda_symbol)

# Zeige das charakteristische Polynom
print("\nCharakteristisches Polynom (lambda als Symbol):")
sp.pprint(char_poly)

# Löse das charakteristische Polynom nach Eigenwerten (lambda)
eigenvalues = sp.solve(char_poly, lambda_symbol)

print("\nDeterminante der Matrix:")
sp.pprint(matrix.det())

# Zeige die berechneten Eigenwerte
cntr = 0
print("\nEigenwerte der Matrix:")
for ev in eigenvalues:
    sp.pprint(ev)
    cntr = cntr + ev

print("\nSpur der Matrix:")
sp.pprint(cntr)