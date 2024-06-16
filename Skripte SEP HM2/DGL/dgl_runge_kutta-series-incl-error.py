import numpy as np
import matplotlib.pyplot as plt

# INPUT

def f(x, y):
    return x/y

def y_exact(x):
    return np.sqrt(x**2-3)

y0 = 1.
a = 2.
b = 5.
h = 0.1
n = int((b-a)/h)
print("n = ", n)

# --------------------------------------------------------------------

"""
def R4_klassisch(f, a, b, n, y0):
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i]+h/2, y[i]+h/2*k1)
        k3 = f(x[i]+h/2, y[i]+h/2*k2)
        k4 = f(x[i]+h, y[i]+h*k3)
        k = 1/6*(k1+2*k2+2*k3+k4)
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*k
    return x, y

x, y_klassisch = R4_klassisch(f, a, b, n, y0)

plt.figure(1)
plt.plot(x, y_klassisch, color="blue", linestyle="--", label="Lösung mit klassischem R4")
plt.plot(x, y_exact(x), color="purple", linestyle=":", label="Exakte Lösung")
plt.legend()
plt.show()
"""


# Eigenes Butcher-Tableau
# 0.25 |
# 0.5  | 0.5
# 0.5  | 0.5 0.5
# 0.75 | 0.75 0.75 0.75
# --------------
#      | 0.1 0.4 0.4 0.1

def RK4_eigen(f, a, b, n, y0):
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    # Achtung: Umbenennung von a und b fuer eigene Koeffizienten
    c = np.array([0.25, 0.5, 0.5, 0.75])
    a = np.array([[0., 0., 0.],
                  [0.5, 0., 0.],
                  [0.5, 0.5, 0.],
                  [0.75, 0.75, 0.75]])
    b = np.array([0.1, 0.4, 0.4, 0.1])
    for i in range(n):
        k1 = f(x[i] + c[0]*h, y[i])
        k2 = f(x[i] + c[1]*h, y[i] + h* a[1,0]*k1)
        k3 = f(x[i] + c[2]*h, y[i] + h*(a[2,0]*k1 + a[2,1]*k2))
        k4 = f(x[i] + c[3]*h, y[i] + h*(a[3,0]*k1 + a[3,1]*k2 + a[3,2]*k3))
        k = b[0]*k1 + b[1]*k2 + b[2]*k3 + b[3]*k4
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*k
    return x, y

# PLOTTEN und Fehler
x, y_eigen = RK4_eigen(f, a, b, n, y0)
plt.figure(2)
plt.plot(x, y_eigen, color="red", linestyle="-", label="Lösung mit eigenem R4")
#plt.plot(x, y_klassisch, color="blue", linestyle="--", label="Lösung mit klassischem R4")
plt.plot(x, y_exact(x), color="purple", linestyle=":", label="Exakte Lösung")
plt.xlabel("x"); plt.ylabel("y"); plt.grid()
plt.legend()
plt.show()

plt.figure(3)
plt.semilogy(x, np.abs(y_eigen-y_exact(x)), color="red", linestyle="-", label="absoluter Fehler mit eigenem R4")
#plt.semilogy(x, np.abs(y_klassisch-y_exact(x)), color="blue", linestyle="-", label="absoluter Fehler mit klassischem R4")
plt.xlabel("x"); plt.grid()
plt.legend()
plt.show()


h_values = [1, 0.1, 0.01, 0.001]
y_exact_5 = y_exact(5.0)

# Fehler berechnen
errors = []
for h in h_values:
    n = int((b - a) / h)
    t, y_numerical = RK4_eigen(f, a, b, n, y0)
    y_5 = y_numerical[-1]
    error = np.abs(y_5 - y_exact_5)
    errors.append(error)
    print(f"h = {h:.6f}, y(5) = {y_5:.6f}, error = {error:.6e}")

# Doppelt logarithmischer Plot
plt.figure()
plt.loglog(h_values, errors, 'o-', label='Fehler')
plt.xlabel('Schrittweite h')
plt.ylabel('Fehler |y(5) - y_exact(5)|')
plt.title('Konvergenz des RK3-Verfahrens')
plt.grid(True, which='both', ls='--')
plt.legend()
plt.show()

# Konvergenzordnung berechnen
log_h = np.log(h_values)
log_errors = np.log(errors)
p = np.polyfit(log_h, log_errors, 1)[0]
print(f"Die Konvergenzordnung des Verfahrens beträgt: {p:.2f}")