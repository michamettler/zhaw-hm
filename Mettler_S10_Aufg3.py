import numpy as np


def Serie10_Aufg3(A, b, x0, tol, opt):
    if opt == 'J':
        return jacobi(A, b, x0, tol)
    elif opt == 'G':
        return gauss_seidel(A, b, x0, tol)


def gauss_seidel(A, b, x0, tol):
    d = np.diag(A)
    D = np.diag(d)
    LplusD = np.tril(A)
    LplusDinv = np.linalg.inv(LplusD)
    RplusD = np.triu(A)
    R = RplusD - D
    B = -LplusDinv @ R
    c = LplusDinv @ b

    return common(x0, tol, B, c)


def jacobi(A, b, x0, tol):
    d = np.diag(A)
    D = np.diag(d)
    LplusR = A - D
    Dinv = np.linalg.inv(D)
    B = -Dinv @ LplusR
    c = Dinv @ b

    return common(x0, tol, B, c)


def common(x0, tol, B, c):
    Bnorm = np.linalg.norm(B, np.inf)
    if Bnorm >= 1:
        raise ValueError('Bnorm >= 1')

    x1 = B @ x0 + c
    n = 1

    # a-priori
    n2 = np.log(tol * (1 - Bnorm) / np.linalg.norm(x1 - x0, np.inf)) / np.log(Bnorm)

    while Bnorm / (1 - Bnorm) * np.linalg.norm(x1 - x0, np.inf) >= tol:
        x0 = x1
        x1 = B @ x0 + c
        n += 1
    return x1, n, n2


# Test
A = np.array([[8., 5., 2.],
              [5., 9., 1],
              [4., 2., 7.]])
b = np.array([19., 5., 34.])
x0 = np.array([1., -1., 3.])

print('Jacobi-Verfahren: 0', Serie10_Aufg3( A, b, x0, 1e-4, 'J'))
print('Gauss-Seidel-Verfahren: 0', Serie10_Aufg3( A, b, x0, 1e-4, 'G'))
