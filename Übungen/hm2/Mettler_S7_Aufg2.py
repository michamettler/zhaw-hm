import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import scipy.optimize

x_data = np.array([2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. , 7.5, 8. ,
       8.5, 9. , 9.5])

y_data = np.array([159.57209984, 159.8851819 , 159.89378952, 160.30305273,
       160.84630757, 160.94703969, 161.56961845, 162.31468058,
       162.32140561, 162.88880047, 163.53234609, 163.85817086,
       163.55339958, 163.86393263, 163.90535931, 163.44385491])
n = np.size(x_data)

x, lam0, lam1, lam2, lam3 = sp.symbols('x, lam0, lam1, lam2, lam3')
f = (lam0 + lam1*10**(lam2 + lam3*x)) / (1 + 10**(lam2 + lam3*x))
m = 4

g = sp.Matrix([y_data[i] - f.subs(x, x_data[i]) for i in range(n)])

lam = sp.Matrix([lam0, lam1, lam2, lam3])
Dg = g.jacobian(lam)

g = sp.lambdify([[lam0, lam1, lam2, lam3]], g, 'numpy')
Dg = sp.lambdify([[lam0, lam1, lam2, lam3]], Dg, 'numpy')

f = sp.lambdify([x, lam0, lam1, lam2, lam3], f, 'numpy')

lam = np.array([100., 120., 3., -1.])
tol = 10**-5
delta = np.array([1., 1., 1., 1.])
i = 1
imax = 20
while np.linalg.norm(delta, 2) >= tol and i <= imax:
    Q, R  = np.linalg.qr(Dg(lam))
    delta = np.linalg.solve(R, -Q.T @ g(lam).flatten())
    k = 0
    kmax = 5
    while (np.linalg.norm(g(lam + delta/2**k), 2)**2 >= np.linalg.norm(g(lam), 2)**2) and k <= kmax:
        k += 1
    if k == kmax + 1:
        k = 0
    lam = lam + delta/2**k
    print('i = ', i)
    print('lam = ', lam)
    print('k = ', k)
    print('||delta|| = ', np.linalg.norm(delta, 2))
    print('||g(lam)||**2 = ', np.linalg.norm(g(lam), 2)**2)
    i = i + 1
lamopt = lam

# Plot
plt.plot(x_data, y_data, marker='o', linestyle='', color='black')
xplot = np.arange(2, 9.5, 0.01)
yplot = f(xplot, lamopt[0], lamopt[1], lamopt[2], lamopt[3])
plt.plot(xplot, yplot, color='red')
plt.xlabel('x'); plt.ylabel('y'); plt.grid(True)
plt.show()

def E(lam):
    E = 0
    for i in range(n):
        E += (y_data[i] - f(x_data[i], lam[0], lam[1], lam[2], lam[3]))**2
    return E
lamstart = np.array([100., 120., 3., -1.])
lamscipy = scipy.optimize.fmin(E, lamstart)
print('lamscipy = ', lamscipy)