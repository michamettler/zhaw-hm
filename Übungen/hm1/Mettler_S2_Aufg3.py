# Hoehere Mathematik 1 - Serie 2 Aufgabe 3a und 3b Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt


n = 6

def archimedesOld(x):
    return np.sqrt(2 - 2* np.sqrt(1 - (x**2 / 4)))

def archimedesNew(x):
    return np.sqrt(x**2 / (2*(1 + np.sqrt(1 - x**2/4))) )

n = 6
sOld = 1.0
sNew = 1.0
iterations = 50
areaOld = np.zeros(iterations + 1)
areaOld[0] = 6.0
areaNew = np.zeros(iterations + 1)
areaNew[0] = 6.0

for i in range(1, iterations + 1):
    n = 2*n
    sOld = archimedesOld(sOld)
    areaOld[i] = n * sOld
    sNew = archimedesNew(sNew)
    areaNew[i] = n * sNew

# Plotten
x = np.arange(iterations + 1)

plt.grid()
plt.plot(x, areaOld)
plt.plot(x, areaNew)
plt.xlabel('Iterationen')
plt.title('Archimedes')

# Erklärung a)
# Der Wert geht erst auf 12 und sackt dann ab 
# Probleme: Minus in Formel, zu grosses n (eps)

# Erklärung b)
# Sobald keine gefährlichen Operatioenn mehr enthalten sind,
# ist das Resultat nicht mehr verfälscht