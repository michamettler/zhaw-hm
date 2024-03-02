import sympy as sp

x, y , z = sp.symbols('x, y, z')

# a
f1 = 5*x*y
f2 = x**2 * y**2 + x + 2*y

f = sp.Matrix([f1, f2])
Df = f.jacobian([x, y])
Df0 = Df.subs({x: 1., y: 2.})
print("Teilaufgabe a)", Df0)

# b
f1 = sp.log(x**2 + y**2) + z
f2 = sp.exp(y**2 + z**2) - x**2
f3 = 1 / (z**2 + x**2) + y**2

f = sp.Matrix([f1, f2, f3])
Df = f.jacobian([x, y, z])
Df0 = Df.subs({x: 1., y: 2., z: 3.})
print("Teilaufgabe b)", Df0)