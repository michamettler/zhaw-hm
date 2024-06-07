import numpy as np

# Datenpaare
n = 3
x_data = np.array([1., 2., 5.])
y_data = np.array([12., 3., 6.])

# Basisfunktionen
m = 2
def f1(x):
    return 1./x

def f2(x):
    return x

# Ansatzfunktionen
def f(x, lam):
    return lam[0]*f1(x) + lam[1]*f2(x)

# Basisfunktionenwertematrix
A = np.zeros((n, m))
for i in range(n):
    A[i, :] = np.array([f1(x_data[i]), f2(x_data[i])])
print(A)
# [[1.  1. ]
#  [0.5 2. ]
#  [0.2 5. ]]

# Loesen des Normalengleichungssystem ohne QR-Zerlegung
B = A.T @ A
c = A.T @ y_data
print(B)
# [[ 1.29  3.  ]
#  [ 3.   30.  ]]
print(c)
# [14.7 48. ]

lam_ohne = np.linalg.solve(B, c)
print(lam_ohne)
# [10.   0.6]

# Loesen des Normalengleichungssystem mit QR-Zerlegung
Q, R = np.linalg.qr(A)
print(Q)
# [[-0.88045091  0.2762632 ]
#  [-0.44022545 -0.1744802 ]
#  [-0.17609018 -0.94511093]]
print(R)
# [[-1.13578167 -2.64135272]
#  [ 0.         -4.7982555 ]]

c = Q.T @ y_data
print(c)
# [-12.94262832  -2.8789533 ]

lam_mit = np.linalg.solve(R, c)
print(lam_mit)
# [10.   0.6]
