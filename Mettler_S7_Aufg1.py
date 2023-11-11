# Hoehere Mathematik 1 - Serie 7 Aufgabe 3 Micha Mettler (mettlmi1)

# Imports
import numpy as np
import matplotlib.pyplot as plt

x_year = np.array([1997., 1999., 2006., 2010.]) - 1997
y_days = np.array([150., 104., 172., 152.])


# a) Gleichungssystem aufstellen uunbd plotten
A = np.array([
    [x_year[0] ** 3, x_year[0] ** 2, x_year[0], 1],
    [x_year[1] ** 3, x_year[1] ** 2, x_year[1], 1],
    [x_year[2] ** 3, x_year[2] ** 2, x_year[2], 1],
    [x_year[3] ** 3, x_year[3] ** 2, x_year[3], 1],
])
b = np.copy(y_days)
c = np.linalg.solve(A, b)
print('c = ', c)
# Resultat: c =  [ -0.38250638   7.84249084 -37.15495615 150.        ]

plt.figure(1)
plt.plot(x_year, y_days)
x_plot = np.arange(0, 15, 0.1)
y_plot = np.polyval(c, x_plot)
plt.plot(x_plot, y_plot)
plt.grid()
plt.ylim([0, 200])
plt.show()


# b)
x_estimated = np.array([2003., 2004.]) - 1997
y_estimated = np.polyval(c, x_estimated)
print('estimated = ', y_estimated)
# Resultat: estimated =  [126.77855478 142.997669  ]

plt.figure(2)
plt.plot(x_year, y_days)
plt.plot(x_estimated, y_estimated)
x_plot = np.arange(0, 15, 0.1)
y_plot = np.polyval(c, x_plot)
plt.plot(x_plot, y_plot)
plt.grid()
plt.ylim([0, 200])
plt.show()


# c)
c_new = np.polyfit(x_year, y_days, 3)
print('c_new = ', c_new)
# Resultat: c_new =  [ -0.38250638   7.84249084 -37.15495615 150.        ]

plt.figure(3)
plt.plot(x_year, y_days)
plt.plot(x_estimated, y_estimated)
x_new = x_plot
y_new = np.polyval(c_new, x_new)
plt.plot(x_new, y_new)
plt.grid()
plt.ylim([0, 200])
plt.show()