import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def differentiate_and_plot_function(function, start, end):
    # Define the symbol x for sympy
    x = sp.symbols('x')
    
    # Convert the input string to a sympy expression
    parsed_function = sp.sympify(function)
    
    # Calculate the derivative
    derivative = sp.diff(parsed_function, x)
    
    # Convert sympy functions to numpy functions
    f = sp.lambdify(x, parsed_function, 'numpy')
    f_prime = sp.lambdify(x, derivative, 'numpy')

    # Generate x values for plotting
    x_vals = np.linspace(start, end, 400)

    # Compute y values for the function and its derivative
    y_vals = f(x_vals)
    y_prime_vals = f_prime(x_vals)

    # Plot the function and its derivative
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=str(parsed_function))
    plt.plot(x_vals, y_prime_vals, label=str(derivative) + ' (derivative)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function and its Derivative')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.xlim(start, end)  # Set x-axis limits
    plt.ylim(start, end)  # Set y-axis limits to the same as x-axis
    plt.legend()
    plt.show()

    return derivative

# Example usage
input_function = "log(sqrt(x) + 2)"
interval_start = -2
interval_end = 2
derivative = differentiate_and_plot_function(input_function, interval_start, interval_end)
print("The derivative of", input_function, "is", derivative)
