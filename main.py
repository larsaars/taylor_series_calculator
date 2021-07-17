import math as m
import matplotlib.pyplot as plt
import numpy as np

from config import *

base_taylor_expr = Integer(0)
current_function = BASE_EXPR

for k in range(GRADE + 1):
    derivative_k = Derivative(current_function, x).doit()
    derivative_k_solved = solve(Eq(derivative_k, DEVELOPMENT_POINT), x)
    derivative_k_numeric_value = 0

    if len(derivative_k_solved) == 0:
        print(f'stopped at grade {k}')
        break
    else:
        derivative_k_solved = derivative_k_solved[0]

    base_taylor_expr += (derivative_k_solved / m.factorial(k)) * ((x - DEVELOPMENT_POINT) ** k)

    current_function = derivative_k

# print resulting taylor expression
print('f(x) = ' + str(BASE_EXPR))
print(f'T({GRADE}, {DEVELOPMENT_POINT})(x) = ' + str(base_taylor_expr))

# and plot both expressions (base_expr and base_taylor_expr)
lam_base_expr = lambdify(x, BASE_EXPR, modules=['numpy'])
lam_taylor_expr = lambdify(x, base_taylor_expr, modules=['numpy'])

x_vals = np.linspace(PLOT_MIN_X, PLOT_MAX_X, PLOT_POINTS)
y_vals_base_expr, y_vals_taylor_expr = lam_base_expr(x_vals), lam_taylor_expr(x_vals)

plt.plot(x_vals, y_vals_base_expr, label='f(x)')
plt.plot(x_vals, y_vals_taylor_expr, label=f'T({GRADE}, {DEVELOPMENT_POINT})(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
