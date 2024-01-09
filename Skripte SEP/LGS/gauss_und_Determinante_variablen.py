import sympy as sp

A = sp.Matrix([[  20, 10, 0],
               [50, 30, 20],
               [ 200, 150, 100]])
b = sp.Matrix([150, 470, 2150])

# Function to perform and display steps of Gaussian elimination
def gaussian_elimination(A, b):
    # Augment the matrix A with vector b
    Ab = A.row_join(b)
    print("Initial Augmented Matrix [A|b]:")
    sp.pprint(Ab)
    print("\n")

    # Number of rows
    nrows = Ab.rows

    # Perform Gaussian elimination
    for i in range(nrows):
        # Normalize the pivot row
        if Ab[i, i] != 0:
            Ab[i, :] = Ab[i, :] / Ab[i, i]
            print(f"Step {i+1}: Normalize row {i+1}")
            sp.pprint(Ab)
            print("\n")

        # Eliminate entries below the pivot
        for j in range(i + 1, nrows):
            Ab[j, :] = Ab[j, :] - Ab[j, i] * Ab[i, :]
            print(f"Step {i+1}.{j+1}: Eliminate entry in row {j+1}, column {i+1}")
            sp.pprint(Ab)
            print("\n")

    # Back substitution
    x = sp.zeros(nrows, 1)
    for i in range(nrows - 1, -1, -1):
        x[i] = Ab[i, -1] - sum(Ab[i, j] * x[j] for j in range(i + 1, nrows))
        print(f"Back Substitution for x[{i+1}]:")
        sp.pprint(x)
        print("\n")

    return x

# Solve the system Ax = b
solution = gaussian_elimination(A, b)

print("Final Solution:")
sp.pprint(solution)

# Calculate and print the determinant of A
det_A = A.det()
print("\nDeterminant of A:", det_A)
