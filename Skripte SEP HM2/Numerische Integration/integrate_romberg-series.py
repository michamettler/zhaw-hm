import numpy as np

# INPUT
def f(x):
    return 6*x**2 - 2*x
a = 0.; b = 4
m = 4
#-----------------------------------------------


def sum_trapez(f, a, b, h):
    n = int((b-a)/h)
    result = (f(a) + f(b))/2
    for i in range(1, n):
        xi = a + i*h
        result += f(xi)
    return result*h

# Romberg-Verfahren
def sum_romberg(f, a, b, m):
    T = np.zeros((m+1, m+1))
    
    h = b - a
    for j in range(0, m+1):
        T[j, 0] = sum_trapez(f, a, b, h/2**j)
        
    for k in range(1, m+1):
        for j in range(0, m-k+1):
            T[j, k] = (4.**k * T[j+1, k-1] - T[j, k-1]) / (4.**k - 1.)
    
    E =  T[0, m]
    return E, T

E, T = sum_romberg(f, a, b, m)
print(E)
print(T)