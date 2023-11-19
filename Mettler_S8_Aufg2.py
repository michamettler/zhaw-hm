# ----------------------------------------------------------------------------
# HM1 SERIE 8 AUFGABE 2 / adel
# ---------------------------------------------------------------------------

import numpy as np


# TEILAUFGABE a)

# Ersetzen Sie alle mit ??? gekennzeichneten Stellen durch passenden Code.

def Serie8_Aufg2(A):
    # Berechnet QR-Zerlegung der nxn-Matrix A mit Householder-Verfahren

    A = np.copy(A)
    n = np.shape(A)[0]

    R = A
    Q = np.eye(n)

    for i in np.arange(0, n - 1):
        a = R[i:, i]
        e = np.zeros(n-i)
        e[0] = 1
        if a[0] >= 0:
            sig = 1
        else:
            sig = -1
        v = a + sig * np.linalg.norm(a) * e
        u = 1 / np.linalg.norm(v) * v
        E = np.eye(n - i)
        u = u.reshape(n - i, 1)
        H = E - 2 * u * u.T
        Qi = np.eye(n)
        Qi[i:n, i:n] = H
        R = Qi @ R
        Q = Q @ Qi.T

    return Q, R


# TEILAUFGABE b)

# Kontrollieren Sie Ihre Ergebnisse aus Aufgabe 1 der Serie 8
# mit der Funktion aus a) und weiterem Code

A = np.array([[1., -2., 3.],
              [-5., 4., 1.],
              [2., -1., 3.]])
b = np.array([1., 9., 5.])
Q, R = Serie8_Aufg2(A)
print(Q)
print(R)
x = np.linalg.solve(R, Q.T@b)
print(x)
