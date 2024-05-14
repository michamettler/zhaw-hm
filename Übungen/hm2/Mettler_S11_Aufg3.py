import numpy as np
import matplotlib.pyplot as plt
from Mettler_S11_Aufg1 import Serie11_Aufg1

#Euler-Verfahren
def euler(f, a, b, n, y0):
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    for i in range(n):
        k = f(x[i], y[i])
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*k
    return x, y

# Modified Euler-Verfahren
def modified_euler(f, a, b, n, y0):
    x = np.zeros(n+1)
    x[0] = a
    y = np.zeros(n+1)
    y[0] = y0
    h = (b-a)/n
    for i in range(n):
        x[i+1] = x[i] + h
        k1 = f(x[i], y[i])
        yE = y[i] + h*k1
        k2 = f(x[i+1], yE)
        k = (k1 + k2)/2
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h*k
    return x, y

def Serie11_Aufg3(f, a, b, n, y0):
    x, y_euler = euler(f, a, b, n, y0)
    x, y_modified_euler = modified_euler(f, a, b, n, y0)
    return x, y_euler, y_modified_euler

def f(x, y):
    return x**2/y
a = 0.
b = 1.4
n = 2
y0 = 2.
x, y_euler, y_modified_euler = Serie11_Aufg3(f, a, b, n, y0)
print('x:', x)
print('y_euler:', y_euler)
print('y_modified_euler:', y_modified_euler)

xmin = -0.5
xmax = 1.5
ymin = 2.
ymax = 2.5
hx = 0.25
hy = 0.1
Serie11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy)

def y(x):
    return np.sqrt(2*x**3/3 + 4)
xplot = np.arange(xmin, xmax, (xmax-xmin)/100.)
plt.plot(xplot, y(xplot), color='red', label='exakt')
plt.plot(x, y_euler, marker='o', linestyle='', color='orange', label='Euler')
plt.plot(x, y_modified_euler, marker='o', linestyle='', color='purple', label='Modifizierter Euler')
plt.grid()
plt.legend()
plt.show()