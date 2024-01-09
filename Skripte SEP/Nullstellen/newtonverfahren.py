import sympy as sy

# Define the symbol x
x = sy.symbols('x')

# Function and its derivatives
f = sy.exp(x**2) + x**-3 - 10
df = sy.diff(f, x)
d2f = sy.diff(df, x)

# Convert to numerical functions
fl = sy.lambdify(x, f)
dfl = sy.lambdify(x, df)
d2fl = sy.lambdify(x, d2f)

print("f'(x) = " + str(df))

# Initial guess
x0 = 2
max_error = 1e-6
max_iterations = 100  # Maximum number of iterations

# Newton-Raphson iteration
xn = [x0]
n = 0
print("n = 0: x0 = " + str(x0))

while n < 1 or (abs(xn[n] - xn[n - 1]) > max_error and n < max_iterations):
    xn.append(xn[n] - fl(xn[n]) / dfl(xn[n]))
    n += 1
    print("n = " + str(n) + ": x" + str(n) + " = " + str(xn[n]) + ", Δ = " + str(abs(xn[n] - xn[n - 1])))

# Check for convergence
if n == max_iterations:
    print("Maximum iterations reached without convergence.")
else:
    print("Converged to:", xn[-1])
