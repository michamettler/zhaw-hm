import numpy as np
import matplotlib.pyplot as plt

# INPUT

# Mit
# z1(t) = x(t)
# z2(t) = x'(t)
# ergibt sich
# z1'(t) = z2(t)
# z2'(t) = -5*z2(t)^2/m - 570000/m

m = 97000.; c = 570000.
x0 = 0.; v0 = 100.

a = 0.; b = 20.; h = 0.1
n = int((b-a)/h)

t = np.zeros(n+1)
z = np.zeros([n+1,2])

t[0] = a
z[0,:] = np.array([x0,v0])

def f(t,z):
    return np.array([z[1], -5*z[1]**2/m - c/m])

# --------------------------------------------------------------------

for i in range(n):
    tM = t[i] + h/2
    zM = z[i,:] + h/2*f(t[i], z[i,:])
    t[i+1] = t[i] + h
    z[i+1,:] = z[i,:] + h*f(tM, zM)

plt.plot(t, z[:,0], t, z[:,1])
plt.xlabel('Zeit [s]'); plt.ylabel('Weg [m] bzw. Geschw. [m/s]')
plt.legend(['Weg', 'Geschwindigkeit'])
plt.grid('True')
plt.show()

# TEILAUFGABE c): Ablesen von Bremszeit und Bremsweg aus Grafik oder 
# wie nachfolgend Bestimmung aus numerischen Ortswerten

i = np.argmax(z[:,0]) # Index zum groessten Ort
print('Bremszeit =', t[i])
print('Bremsweg =', z[i,0])
