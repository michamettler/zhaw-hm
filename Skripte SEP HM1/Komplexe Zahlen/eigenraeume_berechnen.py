import sympy as sp

A = sp.Matrix([
    [13, -4],
    [30, -9],
])

def calculate_eigenspaces(A):
    A = sp.Matrix(A)
    eigenval = A.eigenvals()

    # Calculate the eigenspace for each eigenvalue
    eigenspaces = {}
    for eigenvalue in eigenval:
        # Form the matrix (A - lambda I)
        mat = A - eigenvalue * sp.eye(A.shape[0])

        # Solve the system (A - lambda I)x = 0 to find the eigenspace
        eigenspace = mat.nullspace()
        eigenspaces[eigenvalue] = eigenspace
        print(f"Eigenspace for eigenvalue {eigenvalue}: {eigenspace}")

    return eigenspaces

print(calculate_eigenspaces(A))