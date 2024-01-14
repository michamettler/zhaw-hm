import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# INPUT
x = sp.symbols('x')
meine_funktion = x**2 * sp.exp(-x)

"""
def K(x):
    return sp.exp(x)*sp.Abs((x**2*sp.exp(-x) - 2*x*sp.exp(-x))/x) #Resultat der Kondition einfügen
"""

# Werte für x0 und den maximalen relativen Fehler
x0 = sp.pi / 3
maximaler_relativer_fehler = 0.1  # 10%

# Intervall für Plot
interval = np.arange(-2*np.pi,3*np.pi,10**-4)


# Ableitung der Funktion
ableitung = sp.diff(meine_funktion, x)

# Berechnung Kondition
kondition = abs(ableitung * x / meine_funktion)
kondition_x0 = kondition.subs(x, x0).evalf()

# Berechnung des maximal zulässigen absoluten Fehlers in x0
maximaler_absoluter_fehler = maximaler_relativer_fehler / kondition_x0 * x0

#Berechnung Grenzwerte
def grenzwert_konditionszahl_bei_null():
    # Berechne den Grenzwert der Konditionszahl für x → 0
    grenzwert = [kondition.subs(x, 10**-n).evalf() for n in range(1,6)]
    return grenzwert

def grenzwert_konditionszahl_bei_unendlich():
    # Berechne den Grenzwert der Konditionszahl für x → 0
    grenzwert = [kondition.subs(x, 10**n).evalf() for n in range(1,6)]
    return grenzwert

# Halblogarithmisch plotten
#plt.semilogy(interval,K(interval))
#plt.xlabel('x'); plt.ylabel('K(x)'); plt.grid()   


# Ausgaben
print("Konditionszahl der Funktion als Funktion von x:", kondition)
print("Maximaler absoluter Fehler:", maximaler_absoluter_fehler.evalf())

grenzwert_bei_null = grenzwert_konditionszahl_bei_null()
print("Konditionszahl der Funktion mit x => 0:", grenzwert_bei_null)
#grenzwert_bei_unendlich = grenzwert_konditionszahl_bei_unendlich()
#print("Konditionszahl der Funktion mit x => Unendlich:", grenzwert_bei_unendlich)