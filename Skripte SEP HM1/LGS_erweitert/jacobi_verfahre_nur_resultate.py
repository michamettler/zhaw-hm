import sympy as sp


def jacobi_iterate(a: sp.Matrix, b: sp.Matrix, x: sp.Matrix, precision: int = -1) -> sp.Matrix:
    res = sp.zeros(x.rows, x.cols)

    for i in range(a.rows):
        s = 0
        s_expr = ''

        for j in range(a.cols):
            if i != j:
                s += a[i, j] * x[j]
                s_expr += f' + ({sp.latex(a[i, j])} \\cdot {sp.latex(x[j])})'

        res[i] = (1 / a[i, i]) * (b[i] - s)
        if precision != -1:
            res[i] = res[i].evalf(precision)

        print(
            print(f'x_{{ {i} }} = {(res[i])}')
        )
    return res


def jacobi(a: sp.Matrix, b: sp.Matrix, x0: sp.Matrix, n: int = 100, precision: int = -1) -> sp.Matrix:
    x = x0
    for i in range(n):
        print(f'Iteration {i + 1}')
        x = jacobi_iterate(a, b, x, precision)
    return x

x = sp.symbols('x')

a = sp.Matrix([
    [30, 10, 5],
    [10, x, 20],
    [5, 20, 50],
])

b = sp.Matrix([5*x, x, 5*x])
x0 = sp.Matrix([x, 0, x])

x = jacobi(a, b, x0, 1, 6).evalf()
print(x)