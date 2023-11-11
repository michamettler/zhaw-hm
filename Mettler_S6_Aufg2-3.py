# Hoehere Mathematik 1 - Serie 6 Aufgabe 2 Micha Mettler (mettlmi1)

# Imports
import numpy as np


# Aufgabe 2
def S6_Aufg2(A, b):
    n = np.size(b)
    M = np.zeros((n, n + 1))

    M[0:n, 0:n] = np.copy(A)
    M[0:n, n] = np.copy(b)
    
    for j in range (0, n-1):
        
        # Zeilenvertauschung
        if M[j,j] == 0:
            i = j+1
            while M[i,j] == 0:
                i = i+1
            temp = np.copy(M[i, j : n + 1])
            M[i, j : n + 1] = M[j, j : n + 1]
            M[j, j : n + 1] = temp
        
        # Suubtraktion
        for i in range(j + 1, n):
            c = M[i, j] / M[j, j]
            M[i, j] = 0
            M[i, j + 1 : n + 1] = M[i, j + 1 : n + 1] - c * M[j, j + 1 : n + 1]
        
    # Rückwärtseinsetzen
    x = np.zeros(n)
    for i in np.arange(n-1,-1,-1):
        x[i] = (M[i,n] - np.sum(M[i,i+1:n]*x[i+1:n]))/M[i,i]
        
    return M, x

# Aufgabe 3
A = np.array([[20, 30, 10], [10, 17, 6], [2, 3, 2]])
b = np.array([5200, 3000, 760])

M, x = S6_Aufg2(A,b)

print(M)
print(x)
