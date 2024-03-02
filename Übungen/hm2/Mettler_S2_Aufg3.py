import sympy as sp

x, y , z = sp.symbols('x, y, z')
A = sp.Matrix([x, y, z])

f1 = x + y**2 - z**2 - 13
f2 = sp.log(y/4) + sp.exp(0.5*z - 1) - 1
f3 = (y - 3)**2 - z**3 + 7
f = sp.Matrix([f1, f2, f3])
Df = f.jacobian(A)

x0 = sp.Matrix([3, 4, 2])

fx0 = f.subs({x: x0[0], y: x0[1], z: x0[2]})
Dfx0 = Df.subs({x: x0[0], y: x0[1], z: x0[2]})

g = fx0 + Dfx0*(A - x0)
print(g)