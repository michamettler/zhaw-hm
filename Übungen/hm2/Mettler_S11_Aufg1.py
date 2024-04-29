import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 1
def Serie11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy):
    
    x = np.arange(xmin, xmax+hx, hx)
    y = np.arange(ymin, ymax+hy, hy)
    X, Y = np.meshgrid(x, y)
    m, n = np.shape(X)
    
    DX = np.ones((m, n))
    DY = f(X, Y)
    
    # Pfeile auf gleiche Länge
    DX = DX/(DX**2 + DY**2)**0.5
    DY = DY/(DX**2 + DY**2)**0.5
    
    plt.quiver(X, Y, DX, DY)
    
    plt.xlim([xmin-hx, xmax+hx])
    plt.ylim([ymin-hy, ymax+hy])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()
    
    
# Aufgabe 2
def f(x, y):
    return x**2/y
xmin = -1.
xmax = 2.
ymin = 1.
ymax = 4.
hx = 0.5
hy = 0.5

Serie11_Aufg1(f, xmin, xmax, ymin, ymax, hx, hy)