import numpy as np
import matplotlib.pyplot as plt

# INPUT

x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0.54, 0.44, 0.28, 0.18, 0.12, 0.08])
n = np.size(x_data)

# Je nachdem Anzahl Polynome anpassen

def f1(x):
    return x**4
def f2(x):
    return x**3
def f3(x):
    return x**2
def f4(x):
    return x
def f5(x):
    return 1
m = 5

A = np.zeros((n, m))
for i in range(0, n):
    A[i, 0:m] = np.array([f1(x_data[i]), f2(x_data[i]), f3(x_data[i]), f4(x_data[i]), f5(x_data[i])])

A_T = np.transpose(A)
lam = np.linalg.solve(A_T @ A, A_T @ y_data)
print('lam =', lam) # Koeffizienten des Polynoms

Q, R = np.linalg.qr(A)
Q_T = np.transpose(Q)
lam_qr = np.linalg.solve(R, Q_T @ y_data)
print('lam_qr =', lam_qr)

print('||lam - lam_qr|| =', np.linalg.norm(lam - lam_qr))

x_plot = np.linspace(x_data.min(), x_data.max(), 101)
y_plot = np.polyval(lam[::-1], x_plot)  # Reverse order of lam for np.polyval
y_plot_qr = np.polyval(lam_qr[::-1], x_plot)  # Reverse order of lam_qr for np.polyval

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

lam_poly = np.polyfit(x_data, y_data, 4)  # Fit a 4th order polynomial
print('lam_poly =', lam_poly)
print('||lam - lam_poly|| =', np.linalg.norm(lam - lam_poly[::-1]))  # Compare correctly ordered lam

E = np.linalg.norm(y_data - A @ lam, 2)**2
E_qr = np.linalg.norm(y_data - A @ lam_qr, 2)**2
E_poly = np.linalg.norm(y_data - np.polyval(lam_poly, x_data), 2)**2  # Use np.polyval for E_poly
print('E =', E)
print('E_qr =', E_qr)
print('E_poly =', E_poly)
