import sympy as sp

# Definition der Symbole
x = sp.Symbol('x')
y = sp.Function('y')(x)

# Gegebene Differentialgleichung
diff_eq = sp.Eq(y.diff(x, 3) - (y.diff(x))**2 + x*y, 0)

# Anfangsbedingungen
initial_conditions = {y.subs(x, 0): 2, y.diff(x).subs(x, 0): 1, y.diff(x, 2).subs(x, 0): 0}

# Definieren der neuen Variablen
z1 = sp.Function('z1')(x)
z2 = sp.Function('z2')(x)
z3 = sp.Function('z3')(x)

# Umwandlung der ursprünglichen Differentialgleichung in ein System erster Ordnung
# z1 = y, z2 = y', z3 = y''
dz1_dx = z2
dz2_dx = z3
dz3_dx = (z2)**2 - x*z1

# Zusammenstellen des Systems von Differentialgleichungen
f = sp.Matrix([dz1_dx, dz2_dx, dz3_dx])

# Neue Anfangsbedingungen
new_initial_conditions = {z1.subs(x, 0): 2, z2.subs(x, 0): 1, z3.subs(x, 0): 0}

# Anzeige des Ergebnisses
print("Umwandlung der Differentialgleichung höherer Ordnung in ein System erster Ordnung:")
print(f"Gegebene Differentialgleichung:\n{diff_eq}\n")
print("Anfangsbedingungen:")
for cond, val in initial_conditions.items():
    print(f"{cond} = {val}")

print("\nNeue Variablen:")
print("z1 = y")
print("z2 = y'")
print("z3 = y''\n")

print("System von Differentialgleichungen erster Ordnung:")
print(f"d(z1)/dx = {dz1_dx}")
print(f"d(z2)/dx = {dz2_dx}")
print(f"d(z3)/dx = {dz3_dx}\n")

print("In Matrix-Form:")
print(f"zeta'(x) = f(x, zeta(x)), wobei")
print(f"f(x, zeta) = {f}\n")

print("Neue Anfangsbedingungen:")
for var, val in new_initial_conditions.items():
    print(f"{var} = {val}")
