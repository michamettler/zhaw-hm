import numpy as np


def S9_Aufg2(A, A_tilde, b, b_tilde):
    x = np.linalg.solve(A, b)
    x_tilde = np.linalg.solve(A_tilde, b_tilde)
    condA = np.linalg.cond(A, 1)

    relFehlerA = np.linalg.norm(A - A_tilde, 1) / np.linalg.norm(A, np.inf) #change norm here if needed
    relFehlerB = np.linalg.norm(b - b_tilde, 1) / np.linalg.norm(b, np.inf)
    tatFehler = np.linalg.norm(x - x_tilde, 1) / np.linalg.norm(x, np.inf)

    if (condA * relFehlerA < 1):
        maxFehler = condA / (1 - condA * relFehlerA) * (relFehlerA + relFehlerB)
    else:
        maxFehler = np.nan

    return x, x_tilde, maxFehler, tatFehler


A = np.array([
    [240, 120, 80],
    [60, 180, 170],
    [60, 90, 500],
])

b = np.array([3080, 4070, 5030])
A_tilde = np.array([
    [240, 120, 80],
    [60, 180, 170],
    [60, 90, 500],
])
b_tilde = np.array([3234, 4273.5, 5281.5])

x, x_tilde, maxFehler, tatFehler = S9_Aufg2(A, A_tilde, b, b_tilde)
relFehler = np.linalg.norm((x_tilde - x), 1) / np.linalg.norm(x, 1)
print('x: ', x)
print('x_tilde: ', x_tilde)
print('maximaler fehler: ', maxFehler)
print('tatsaechlicher fehler: ', tatFehler)
print('relativer fehler: ', relFehler)
