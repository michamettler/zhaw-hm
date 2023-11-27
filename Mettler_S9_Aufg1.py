import numpy as np


def S9_Aufg2(A, A_tilde, b, b_tilde):
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    condA = np.linalg.cond(A, np.inf)

    relFehlerA = np.linalg.norm(A - A_tilde, np.inf) / np.linalg.norm(A, np.inf)
    relFehlerB = np.linalg.norm(b - b_tilde, np.inf) / np.linalg.norm(b, np.inf)
    tatFehler = np.linalg.norm(x - x_tilde, np.inf) / np.linalg.norm(x, np.inf)

    if (condA * relFehlerA < 1):
        maxFehler = condA / (1 - condA * relFehlerA) * (relFehlerA + relFehlerB)
    else:
        maxFehler = np.nan

    return x, x_tilde, maxFehler, tatFehler


A = np.array([[20000., 30000., 10000.],
              [10000., 17000., 6000.],
              [2000., 3000., 2000.]])
b = np.array([5720000., 3300000., 836000.])
A_tilde = A - 0.1
b_tilde = b + 100
print(S9_Aufg2(A, A_tilde, b, b_tilde))
