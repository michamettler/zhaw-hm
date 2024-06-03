import numpy as np

# INPUT
x = np.array([0., 2500., 5000., 10000.])
y = np.array([1013., 747., 540., 226.])
x_int = 3750.
# -----------------------

def lagrange_int(x, y, x_int):
    n = np.size(x) - 1
    L = np.ones(n+1)
    
    for i in range(n+1):
        for j in range(n+1):
            if i != j:
                L[i] *= (x_int - x[j]) / (x[i] - x[j])
                
    y_int = 0
    for i in range(n+1):
        y_int += y[i] * L[i]
    return y_int



y_int = lagrange_int(x, y, x_int)
print('y_int =', y_int)