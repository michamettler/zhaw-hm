# Hoehere Mathematik 1 - Serie 1 Aufgabe 1 Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt

# Input:
#   Koeffizientenliste (a, [a0, a1, a2, ..., an]),
#   Intervall-Untergrenze (xmin),
#   Intervall-Obergrenze (xmax)
# Output:
#   x: Vektor [x0, x1, ..., xm] mit xmin <= xi <= xmax mit Step 0.01
#   p: Vektor mit Funktionswerten
#   dp: Vektor mit Funktionswerten der Ableitungsfunktion
#   pint: Vektor mit Funktionswerten der Stammfunktion
def Mettler_S1_Aufg2(a, xmin, xmax):
    
    # Intervall
    x = np.arange(xmin, xmax, 0.01)
    
    # Grad des Polynoms
    n = np.size(a) - 1
    
    # Polynom an * xm^i
    p = np.zeros(np.size(x))
    for i in range(n+1):
        p += a[i] * x**i
    
    # Polynom Ableitungsfunktion an*i * xm^(i-1)
    dp = np.zeros(np.size(x))
    for i in range(n+1):
        dp += a[i]*i * x**(i-1)
    
    # Polynom Stammfunktion an/(i+1) * xm^(i+1)
    pint = np.zeros(np.size(x))
    for i in range(n+1):
        pint += a[i]/(i+1) * x**(i+1)
    
    return x, p, dp , pint
    

# Functionsaufruf
a = np.array([-4., -3., 2., 1.])
xmin = -4.
xmax = 4.

# Plotten
x, p, dp, pint = Mettler_S1_Aufg2(a, xmin, xmax)
plt.ylim(-10., 10.)
plt.grid()
plt.plot(x, p)
plt.plot(x, dp)
plt.plot(x, pint)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)', 'df(x)', 'F(x)'])
plt.title('Plot von Polynom, Ableitung und Stammfunktion')
plt.show()
    

    