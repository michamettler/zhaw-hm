import numpy as np

def Serie12_Aufg1(f, a, b, n, y0):
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

def f(x, y):
    return x**2 + 0.1*y
a = -1.5
b = 1.5
n = 5
y0 = 0.

x, y = Serie12_Aufg1(f, a, b, n, y0)
print("x = ", x)
print("y = ", y)