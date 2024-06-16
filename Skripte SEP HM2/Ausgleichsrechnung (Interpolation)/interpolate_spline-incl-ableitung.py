import numpy as np
import matplotlib.pyplot as plt
 
# INPUT
x = np.array([0., 0.5, 2., 3.])
y = np.array([1., 2., 2.5, 0.])
 
xx = np.arange(0, 3, 0.1)
 
def spline_interpolation(x, y, xx):
    x = np.array(x)
    y = np.array(y)
    xx = np.array(xx)
   
    n = np.size(x) - 1
   
    h = x[1:n+1] - x[0:n] # step 0
    a = y[0:n] # step 1
   
    # step 2
    c = np.zeros(n+1)
    A = np.zeros((n-1, n-1))
    for i in range(n-1):
        A[i, i] = 2*(h[i] + h[i+1])
    for i in range(0, n-2):
        A[i, i+1] = h[i+1]
        A[i+1, i] = h[i+1]
    z = 3 * ((y[2:n+1] - y[1:n]) / h[1:n] - (y[1:n] - y[0:n-1]) / h[0:n-1])
    c[1:n] = np.linalg.solve(A, z)
   
    # step 3
    b = (y[1:n+1] - y[0:n]) / h - h / 3 * (c[1:n+1] + 2*c[0:n])
   
    # step 4
    d = (c[1:n+1] - c[0:n]) / (3*h)
   
    # evaluate the spline
    m = np.size(xx)
    yy = np.zeros(m)
    for j in range(m):
        i = 0
        while xx[j] > x[i+1]:
            i = i + 1
        t = (xx[j] - x[i])
        yy[j] = np.polyval([d[i], c[i], b[i], a[i]], t)
   
    return yy, a, b, c, d
 
def evaluate_spline_derivatives(a, b, c, d, x, t):
    i = 0
    while t > x[i+1]:
        i += 1
    dt = t - x[i]
    velocity = 3*d[i]*dt**2 + 2*c[i]*dt + b[i]
    acceleration = 6*d[i]*dt + 2*c[i]
    return velocity, acceleration
 
# Interpolate the spline and get the coefficients
yy, a, b, c, d = spline_interpolation(x, y, xx)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
 
# Calculate the velocity and acceleration at t = 1
t = 1
velocity, acceleration = evaluate_spline_derivatives(a, b, c, d, x, t)
print(f"Velocity at t={t}: {velocity}")
print(f"Acceleration at t={t}: {acceleration}")
 
# Plot the spline and the velocity over time
velocities = []
for t in xx:
    v, _ = evaluate_spline_derivatives(a, b, c, d, x, t)
    velocities.append(v)
 
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, y, 'o', label='data points')
plt.plot(xx, yy, '-', label='spline')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
 
plt.subplot(1, 2, 2)
plt.plot(xx, velocities, '-', label='velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.legend()
 
plt.tight_layout()
plt.show()