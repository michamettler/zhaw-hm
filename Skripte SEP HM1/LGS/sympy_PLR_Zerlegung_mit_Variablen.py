import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the matrix A with a symbolic variable
A = sp.Matrix([[20, 10, 0],
               [50, x, 20],
               [200, 150, 100]])

# LU Decomposition with permutation
L, U, perm = A.LUdecomposition()

# Construct the permutation matrix P from the permutation information
P = sp.eye(A.rows).permute(perm)

print("Permutation Matrix P:")
sp.pprint(P)

print("\nMatrix L (Lower triangular):")
sp.pprint(L)

print("\nMatrix R (Upper triangular):")
sp.pprint(U)

# Verify the decomposition
print("\nVerification (P * L * R):")
sp.pprint(P * L * U)
