from sympy import Matrix

# Define the matrix A
A = Matrix([[10**-20, 10**-20], [2, 3]])

# Calculate the 1-norm of the matrix A, which is the maximum absolute column sum of the matrix
A_norm_1 =A.norm(1)

# Calculate the 1-norm of the inverse of A
A_inv_norm_1 = A.inv().norm(1)

# The condition number is the product of the norms of A and its inverse
condition_number = A_norm_1 * A_inv_norm_1
print(condition_number)
