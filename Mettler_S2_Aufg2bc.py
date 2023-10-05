# Hoehere Mathematik 1 - Serie 2 Aufgabe 2b und 1c Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1e-14, 1e-14, 2001)

def g1(x):
    return x / (np.sin(1 + x) - np.sin(1))

def g2(x):
    return x / (2 * np.cos(1 + x / 2) * np.sin(x / 2))

# Plotten
plt.grid()
plt.plot(x, g1(x))
plt.plot(x, g2(x))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['g2(x)'])
plt.title('Auslöschung')

# Erklärung b)
# Nahe 0 wird das Resultat massiv verfälscht

# Erklärung c)
# Keine Subtraktion mehr, deshalb keine Auslöschung und konstante Lösung