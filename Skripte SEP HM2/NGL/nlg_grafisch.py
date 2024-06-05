import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Skalarwertige Funktion mit zwei Variablen
def f(x1,x2):
    return x1**2 - x1*x2**2 + 0.5*x2**3 + 10

# Wertetabelle von f
x1 = np.array([-2., -1., 0., 1., 2.])
x2 = np.array([-2., -1., 0., 1., 2.])
X1, X2 = np.meshgrid(x1, x2)
print('X1 = \n', X1)
print('X2 = \n', X2)

# X1 =
# [[-2. -1.  0.  1.  2.]
#  [-2. -1.  0.  1.  2.]
#  [-2. -1.  0.  1.  2.]
#  [-2. -1.  0.  1.  2.]
#  [-2. -1.  0.  1.  2.]]
# X2 =
# [[-2. -2. -2. -2. -2.]
#  [-1. -1. -1. -1. -1.]
#  [ 0.  0.  0.  0.  0.]
#  [ 1.  1.  1.  1.  1.]
#  [ 2.  2.  2.  2.  2.]]

Y = f(X1, X2)
print('Y = \n', Y)

# Y =
# [[18. 11.  6.  3.  2.]
#  [15.5 11.5  9.5  9.5 11.5]
#  [14.  11. 10. 11. 14.]
#  [16.5 12.5 10.  10.5 12.5]
#  [26.  19. 14. 11. 10.]]

# 3D-Gitterplot von f, weimtaschig (1)
fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X1, X2, Y, color='k')
ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('y')
ax.set_xlim([-2.5, 2.5]); ax.set_ylim([-2.5, 2.5]); ax.set_zlim([-5, 25])

# 3D-Gitterplot von f, engmaschig (2)
x1 = np.arange(-2., 2.1, 0.2)
x2 = np.arange(-2., 2.1, 0.2)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X1, X2, Y, color='k')
ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('y')
ax.set_xlim([-2.5, 2.5]); ax.set_ylim([-2.5, 2.5]); ax.set_zlim([-5, 25])

# 3D-Flaechenplot (3)
fig = plt.figure(3)
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Y, color='violet')
ax.set_xlabel('x1'); ax.set_ylabel('x2'); ax.set_zlabel('y')
ax.set_xlim([-2.5, 2.5]); ax.set_ylim([-2.5, 2.5]); ax.set_zlim([-5, 25])

# 2D-Hoehenlinienplot von f, nur eine Hoehe (4)
fig = plt.figure(4)
cont = plt.contour(X1, X2, Y, levels=[11.], colors=['purple'], linestyles=['dashed'])
plt.xlabel('x1'); plt.ylabel('x2')
plt.xlim([-2.5, 2.5]); plt.ylim([-2.5, 2.5])
plt.grid()

# 2D-Hoehenlinienplot von f, mehrere Hoehen (5)
fig = plt.figure(5)
cont = plt.contour(X1, X2, Y, levels=[8., 9., 10., 11., 12., 13., 14., 15.])
plt.colorbar(cont)
plt.xlabel('x1'); plt.ylabel('x2')
plt.xlim([-2.5, 2.5]); plt.ylim([-2.5, 2.5])
plt.grid()
plt.show()