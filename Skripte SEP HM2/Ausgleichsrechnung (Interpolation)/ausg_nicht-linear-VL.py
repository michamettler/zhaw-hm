import numpy as np
import sympy as sp

# Wertepaare
xdata = np.array([0., 1., 2.])
ydata = np.array([1., 2., 8.])
n = np.size(xdata)

# Ansatzfunktionen f symbolisch
x, lam1, lam2 = sp.symbols('x, lam1, lam2')
f = lam1 * sp.exp(lam2 * x)

# Fehlerfunktional E symbolisch
E = 0
for i in range(n):
    E += (ydata[i] - f.subs(x, xdata[i]))**2

# Ableitung von E
lam = sp.Matrix([lam1, lam2])
print(lam)
# Matrix([[lam1],
#         [lam2]])
E = sp.Matrix([E])
print(E)
# Matrix([[(1.0 - lam1)**2 + 4.0*(-0.5*lam1*exp(1.0*lam2) + 1)**2
#          + 64.0*(-0.125*lam1*exp(2.0*lam2) + 1)**2]])

DE = E.jacobian(lam)
print(DE)
# Matrix([[2*lam1 - 4.0*(-0.5*lam1*exp(1.0*lam2) + 1)*exp(1.0*lam2)
#          - 16.0*(-0.125*lam1*exp(2.0*lam2) + 1)*exp(2.0*lam2) - 2.0,
#          -4.0*lam1*(-0.5*lam1*exp(1.0*lam2) + 1)*exp(1.0*lam2)
#          - 32.0*lam1*(-0.125*lam1*exp(2.0*lam2) + 1)*exp(2.0*lam2)]])

# Nichtlineare Gleichungssystem dE/dlam1 = 0, dE/dlam2 = 0 als
# Nullstellenproblem einer vektorwertigen Funktion F
F = DE.transpose()
# F = [F1],
#     [F2] = [dE/dlam1],
#           [dE/dlam2]

# Loesen von F = 0 mit Newton-Verfahren fuer Systeme
# Ableitung von F symbolisch
DF = F.jacobian(lam)
# [[   dF1/dlam1   ,    dF1/dlam2 ],
#  [   dF2/dlam1   ,    dF2/dlam2 ]]
print(DF)
# 2.0*exp(2.0*lam2) + 2.0*exp(4.0*lam2) + 2

import numpy as np
import sympy as sp

# Wertepaare
xdata = np.array([0., 1., 2.])
ydata = np.array([1., 2., 8.])
n = np.size(xdata)

# Ansatzfunktionen f symbolisch
x, lam1, lam2 = sp.symbols('x, lam1, lam2')
f = lam1 * sp.exp(lam2 * x)

# Fehlerfunktional E symbolisch
E = 0
for i in range(n):
    E += (ydata[i] - f.subs(x, xdata[i]))**2

# Ableitung von E
lam = sp.Matrix([lam1, lam2])
E = sp.Matrix([E])
DE = E.jacobian(lam)

# F, DF und E numerisch
F = sp.lambdify([[lam1, lam2]], F , 'numpy')
DF = sp.lambdify([[lam1, lam2]], DF, 'numpy')
E = sp.lambdify([[lam1, lam2]], E , 'numpy')

# Auswertung von F, DF und E
lam = np.array([0., 0.])
print(F(lam)) # Ergibt 2D-Array.
# [[-22.]
#  [ -0.]]
print(F(lam).flatten()) # Wandelt 2D-Array in 1D-Array um.
# [-22.  -0.]
print(DF(lam))
# [[ -6. -36.]]
print(E(lam)) # Ergibt 2D-Array.
# [[69.]]
print(E(lam)[0,0]) # Ergibt Skalar.
# 69.0

# Newton-Verfahren mit Daempfung numerisch
lam = np.array([0.5, 1.5])
imax = 15
for i in range(1, imax+1):
    delta = np.linalg.solve(DF(lam), -F(lam).flatten())
    kmax = 4
    k = 0
    while (k <= kmax and np.linalg.norm(F(lam + delta/2**k), 2) >= np.linalg.norm(F(lam),2)):
        k = k + 1
    if k == kmax + 1:
        k = 0
    lam = lam + delta/2**k
    print('i =', i, 'k =', k, 'lam =', lam)
    print('||F(lam)|| =', np.linalg.norm(F(lam), 2), 'E(lam) =', E(lam)[0,0])

# ...
# i = 5 k = 3 lam = [0.48193972 1.4046291 ]
# ||F(lam)|| = 1.3769159456754398 E(lam) = 0.2697247469563912
# ...
# i = 10 k = 1 lam = [0.57677051 1.31252952]
# ||F(lam)|| = 1.002689847055175 E(lam) = 0.2009826950366923
# ...
# i = 15 k = 0 lam = [0.614195664 1.28096229]
# ||F(lam)|| = 6.587440745812655e-14 E(lam) = 0.19489713807375045
