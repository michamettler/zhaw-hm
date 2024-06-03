import numpy as np
from numpy.linalg import solve

A = np.array([
    [1, 1, 1],
    [2, 2+2**-52, 5],
    [4, 6, 8],
])
b = np.array([1, 0, 0])

# Definiere die LR-Zerlegung
L = np.array([[1, 0, 0], [2, 1, 0], [4, 2/2**-52, 1]])
R = np.array([[1, 1, 1], [0, 2**-52, 3], [0, 0, 4 - 6/2**-52]])

# Definiere b
b = np.array([1, 0, 0])

# Löse L * y = b für y
y = solve(L, b)

# Löse R * x = y für x
x = solve(R, y)

x1 = solve(A, b)


print("Lösung anhand LR Zerlegung", x)
print("Lösung mit A und b", x1)
