import sympy as sp

def evaluate_function(function, x_value):
    # Define the symbol x
    x = sp.symbols('x')

    # Parse the function
    parsed_function = sp.sympify(function)

    # Evaluate the function at the given x value and return the numeric value
    return parsed_function.subs(x, x_value).evalf()

# Example usage
function_input = "exp(2**2) + x**-3 - 10"  # Function with x only in part of the expression
x_value = 2  # Value at which to evaluate the function

# Evaluate the function and get the numeric result
numeric_result = evaluate_function(function_input, x_value)
print("The numeric value of the function at x =", x_value, "is:", numeric_result)
