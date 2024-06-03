import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# INPUT, mehr weiter unten

x = np.array([0.1, 0.3, 0.7, 1.2, 1.6, 2.2, 2.7, 3.1, 3.5, 3.9], dtype=np.float64)
y = np.array([0.558, 0.569, 0.176, -0.207, -0.133, 0.132, 0.055, -0.090, -0.069, 0.027], dtype=np.float64)

lam0 = np.array([1, 2, 2, 1],dtype=np.float64)
tol = 1e-5

p = sp.symbols('p0 p1 p2 p3')

def f(x,p):
    return (p[0]*sp.exp(-p[1]*x)*sp.sin(p[2]*x+p[3]))

# --------------------------------------------------------

g = sp.Matrix([y[k]-f(x[k],p) for k in range(len(x))])

Dg = g.jacobian(p)

g = sp.lambdify([p], g, 'numpy')
Dg = sp.lambdify([p], Dg, 'numpy')

k=0
lam=np.copy(lam0)
[Q,R] = np.linalg.qr(Dg(lam))
delta = np.linalg.solve(R,-Q.T @ g(lam)).flatten() 
lam = lam+delta
increment = np.linalg.norm(delta)

# Fehlerfunktional des Startvektors lam0
err_func0 = np.linalg.norm(g(lam0))**2
# Fehlerfunktional nach der ersten Iteration
err_func = np.linalg.norm(g(lam))**2


# Ohne Dämpfung
def gauss_newton(g, Dg, lam0, tol, max_iter):
    k=0
    lam=np.copy(lam0)
    increment = tol+1
    err_func = np.linalg.norm(g(lam))**2
    
    while increment>=tol and k <= max_iter: #Hier kommt Ihre Abbruchbedingung, die tol und max_iter berücksichtigen muss# 

        # QR-Zerlegung von Dg(lam) und delta als Lösung des lin. Gleichungssystems
        [Q,R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()                                          # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
                                                             # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann           
            
        # Update des Vektors Lambda        
        lam = lam + delta
        err_func = np.linalg.norm(g(lam))**2
        increment = np.linalg.norm(delta)
        k = k+1
        print('Iteration: ',k)
        print('lambda = ',lam)
        print('Inkrement = ',increment)
        print('Fehlerfunktional =', err_func)
    return(lam,k)

# --------------------------------------------------------

# Mit Dämpfung
def gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping):
    k=0
    lam=np.copy(lam0)
    increment = tol+1
    err_func = np.linalg.norm(g(lam))**2
    
    while increment >= tol and k < max_iter:
        # QR-Zerlegung von Dg(lam)
        [Q,R] = np.linalg.qr(Dg(lam))
        delta = np.linalg.solve(R, -Q.T @ g(lam)).flatten()                                                # Achtung: flatten() braucht es, um aus dem Spaltenvektor delta wieder
                                                                     # eine "flachen" Vektor zu machen, da g hier nicht mit Spaltenvektoren als Input umgehen kann           
        # hier kommt die Däfmpfung, falls damping = 1
        p=0
        
        if damping:
            while p < pmax and np.linalg.norm(g(lam+delta/2**p))**2 >= err_func:
                p = p+1
            if p == pmax + 1:
                p = 0
               
        # Update des Vektors Lambda        
        lam = lam + delta/2**p
        err_func = np.linalg.norm(g(lam))**2
        increment = np.linalg.norm(delta/2**p)
        k = k+1
        print('Iteration: ',k)
        print('lambda = ',lam)
        print('Inkrement = ',increment)
        print('Fehlerfunktional =', err_func)
    return(lam,k)





# FINAL INPUT

# DÄMPFUNG
tol = 1e-5
max_iter = 30
[lam_without,n] = gauss_newton(g, Dg, lam0, tol, max_iter)

# OHNE DÄMPFUNG
tol = 1e-5
max_iter = 30
pmax = 5
damping = 1
[lam_with,n] = gauss_newton_d(g, Dg, lam0, tol, max_iter, pmax, damping)

t = sp.symbols('t')
F = f(t,lam_without)
F = sp.lambdify([t],F,'numpy')
t = np.linspace(x.min(),x.max())

plt.plot(x,y,'o')
plt.plot(t,F(t))
plt.xlabel('x')
plt.ylabel('y')
plt.show()