import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the matrix A with a symbolic variable
A = sp.Matrix([[20, 10, 0],
               [50, x, 20],
               [200, 150, 100]])

# LU Decomposition
L, U, _ = A.LUdecomposition()

print("Matrix L (Lower triangular):")
sp.pprint(L)

print("\nMatrix R (Upper triangular):")
sp.pprint(U)

# Define the vector b
b = sp.Matrix([150, 470, 2150])

# Solve the system symbolically
# First, solve Ly = b
y = L.solve(b, method='GJ')  # Using Gauss-Jordan elimination for solving

# Then, solve Ux = y
solution = U.solve(y, method='GJ')  # Using Gauss-Jordan elimination for solving

print("\nSymbolic Solution:")
sp.pprint(solution)
