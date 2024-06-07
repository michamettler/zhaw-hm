# WICHTIG FÜR PRÜFUNG

import numpy as np
import matplotlib.pyplot as plt

# INPUT

x_data = np.arange(0, 110, 10)
y_data = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1,\
                   983.2, 977.8, 971.8, 965.3, 958.4])
n = np.size(x_data)

#------------------

def f1(x):
    return x**2
def f2(x):
    return x
def f3(x):
    return 1
m = 3

A = np.zeros((n, m))
for i in range(0, n):
    A[i, 0:m] = np.array([f1(x_data[i]), f2(x_data[i]), f3(x_data[i])])

A_T = np.transpose(A)
lam = np.linalg.solve(A_T @ A, A_T @ y_data)
print('lam =', lam)

Q, R = np.linalg.qr(A)
Q_T = np.transpose(Q)
lam_qr = np.linalg.solve(R, Q_T @ y_data)
print('lam_qr =', lam_qr)

print('||lam - lam_qr|| =', np.linalg.norm(lam - lam_qr))

x_plot = np.arange(0, 101, 1)
y_plot = np.polyval(lam, x_plot)
y_plot_qr = np.polyval(lam_qr, x_plot)

plt.plot(x_data, y_data, marker='o', color='black', linestyle='', label='Datenpunkte')
plt.plot(x_plot, y_plot, color='red', linestyle='--', label='Normalengleichung ohne QR')
plt.plot(x_plot, y_plot_qr, color='blue', linestyle='-.', label='Normalengleichung mit QR') # i.d.R besser konditioniert als Normalgleichung ohne QR
plt.xlabel('Temperatur')
plt.ylabel('Dichte')
plt.grid()
plt.legend()
plt.show()

print('Konditionszahl von A^T*A bez. 2-er Norm =', np.linalg.cond(A_T @ A, 2))
print('Konditionszahl von R bez. 2-er Norm =', np.linalg.cond(R, 2))


lam_poly = np.polyfit(x_data, y_data, 2)
print('lam_poly =', lam_poly)
print('||lam - lam_poly|| =', np.linalg.norm(lam - lam_poly))

E = np.linalg.norm(y_data - A @ lam, 2)**2
E_qr = np.linalg.norm(y_data - A @ lam_qr, 2)**2
E_poly = np.linalg.norm(y_data - A @ lam_poly, 2)**2
print('E =', E)
print('E_qr =', E_qr)
print('E_poly =', E_poly)