import numpy as np
import matplotlib.pyplot as plt
from Mettler_S9_Aufg2 import S9_Aufg2

m = 100
n = 1000

dxmax = np.zeros(n)
dxobs = np.zeros(n)
for i in range (n):
    A = np.random.rand(m, m)
    b = np.random.rand(m)
    A_tilde = A + np.random.rand(m, m) / 10**5
    b_tilde = b + np.random.rand(m) / 10 ** 5
    x, x_tilde, dxmax[i], dxobs[i] = S9_Aufg2(A, A_tilde, b, b_tilde)

plt.semilogy(range(0,n), dxmax)
plt.semilogy(range(0,n), dxobs)
plt.semilogy(range(0,n), dxmax/dxobs)
plt.grid()
plt.legend()
plt.show()