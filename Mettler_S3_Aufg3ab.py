# Hoehere Mathematik 1 - Serie 3 Aufgabe 3a und 3b Micha Mettler (mettlmi1)

# 3a
# f(x) = 5/(3root(2x^2)) = 5 * 2^(-1/3) * x^(-2/3) => Abstand: log(5 * 2^(-1/3)), Steigung: -2/3
# g(x) = 10^5 * (2e)^(-x/100) = 10^5 * ((2e)^(-x/100))^x => Abstand: log10^5, Steigung: log(2e)^(-x/100) 
# h(x) = (10^2x / 2^5x)^2 = (10^4 / 2^10)^x => Abstand: 0, Steigung: log(10^4 / 2^10)

# 3b
# Imports
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1e-3, 100, 1e-3)

def f(x):
    return 5 * 2**(-1/3) * x**(-2/3)

def g(x):
    return 10**5 * ((2*np.exp(1))**(-x/100))**x

def h(x):
    return (10**4 / 2**10)**x

plt.xlabel('x')
plt.ylabel('y')
plt.figure(1)
plt.loglog(x, f(x)),plt.xlabel("x"), plt.ylabel("f(x)"), plt.grid() 
plt.figure(2)
plt.semilogy(x, g(x)),plt.xlabel("x"), plt.ylabel("g(x)"), plt.grid() 
plt.figure(3)
plt.semilogy(x, h(x)),plt.xlabel("x"), plt.ylabel("h(x)"), plt.grid()