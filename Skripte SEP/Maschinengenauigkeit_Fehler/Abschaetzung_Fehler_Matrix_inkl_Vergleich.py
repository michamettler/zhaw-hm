# ----------------------------------------------------------------------------
# HM1 SERIE 8 AUFGABE 2 / mettlmi1
# ---------------------------------------------------------------------------

import numpy as np

# a)
A = np.array([[20000., 30000., 10000.],
              [10000., 17000., 6000.],
              [2000., 3000., 2000.]])
b = np.array([5720000., 3300000., 836000.])
b_schlange = np.array([5820000., 3400000., 936000.])
A_Inverse = np.linalg.inv(A)

norm_b_minus_bschlange = np.linalg.norm(b - b_schlange, np.inf)
norm_b_schlange = np.linalg.norm(b, np.inf)
norm_A = np.linalg.norm(A, np.inf)
norm_inverse = np.linalg.norm(A_Inverse, np.inf)

print('Teilaufgabe a:', norm_A * norm_inverse * (norm_b_minus_bschlange / norm_b_schlange) * 100, '%')

# b)
A_schlange = np.array([[19900., 29900., 9900.],
                       [9900., 16900., 5900.],
                       [1900., 2900., 1900.]])

norm_A_minus_Aschlange = np.linalg.norm(A_schlange - A, np.inf)
norm_A = np.linalg.norm(A, np.inf)
norm_inverse = np.linalg.norm(A_Inverse, np.inf)
condA = norm_A * norm_inverse

print('Teilaufgabe b:', condA / (1 - condA * norm_A_minus_Aschlange / norm_A) * (
            norm_A_minus_Aschlange / norm_A + (norm_b_minus_bschlange / norm_b_schlange)) * 100, '%')

# c)
x_schlange = np.linalg.solve(A_schlange, b_schlange)
x = np.linalg.solve(A, b)
norm_x_minus_xschlange = np.linalg.norm(x - x_schlange, np.inf)
norm_x = np.linalg.norm(x, np.inf)
print('Vergleich (c)', norm_x_minus_xschlange / norm_x * 100,'%')