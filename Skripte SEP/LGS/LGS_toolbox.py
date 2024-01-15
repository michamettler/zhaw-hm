from sympy import Matrix, symbols

def add_matrices(A, B):
    """Addiert zwei Matrizen."""
    return A + B

def subtract_matrices(A, B):
    """Subtrahiert zwei Matrizen."""
    return A - B

def multiply_matrices(A, B):
    """Multipliziert zwei Matrizen (verwendet die *-Methode)."""
    return A * B

def matrix_mult(A, B):
    """Multipliziert zwei Matrizen (verwendet den @-Operator)."""
    return A @ B

def invert_matrix(A):
    """Invertiert eine Matrix."""
    return A.inv()

def transpose_matrix(A):
    """Transponiert eine Matrix."""
    return A.T

def cross_product(A, B):
    """Berechnet das Kreuzprodukt zweier Matrizen."""
    return A.cross(B)

def determinant(A):
    """Berechnet die Determinante einer Matrix."""
    return A.det()

# Beispiel für die Nutzung der Toolbox mit Variablen
if __name__ == "__main__":
    x, y, z = symbols('x y z')
    A = Matrix([[1, x], [y, 1]])
    B = Matrix([[z, 1], [1, z]])

    print("A + B =", add_matrices(A, B))
    print("A - B =", subtract_matrices(A, B))
    print("A * B (mit *-Methode) =", multiply_matrices(A, B))
    print("A * B (mit @-Operator) =", matrix_mult(A, B))
    print("Invertiert A =", invert_matrix(A))
    print("Transponiert A =", transpose_matrix(A))
    print("Determinante von A =", determinant(A))
    # Für das Kreuzprodukt benötigen wir 3x1-Matrizen
    C = Matrix([1, 2, 3])
    D = Matrix([x, y, z])
    print("Kreuzprodukt C und D =", cross_product(C, D))
