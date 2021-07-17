import math as m
import matplotlib.pyplot as plt
import numpy as np

from config import *

# calc ranges for plotting
PLOT_MIN_X, PLOT_MAX_X = DEVELOPMENT_POINT - PLOT_RANGE, DEVELOPMENT_POINT + PLOT_RANGE
PLOT_POINTS = 1000

# calculate the nth taylor series for the function (BASE_EXPR)
base_taylor_expr = Float(lambdify(x, BASE_EXPR)(DEVELOPMENT_POINT))
current_function = BASE_EXPR

for k in range(1, GRADE + 1):
    derivative_k = Derivative(current_function, x).doit()
    derivative_k_solved = lambdify(x, derivative_k)(DEVELOPMENT_POINT)

    base_taylor_expr += (derivative_k_solved / m.factorial(k)) * ((x - DEVELOPMENT_POINT) ** k)

    current_function = derivative_k

# print resulting taylor expression
print('f(x) = ' + str(BASE_EXPR))
print(f'T({GRADE}, {DEVELOPMENT_POINT})(x) = ' + str(base_taylor_expr))

# and plot both expressions (base_expr and base_taylor_expr)
# by first making functions out of the two expressions,
# then calculating in an linear space N points and plotting those points with matplotlib
lam_base_expr = lambdify(x, BASE_EXPR, modules=['numpy'])
lam_taylor_expr = lambdify(x, base_taylor_expr, modules=['numpy'])

x_vals = np.linspace(PLOT_MIN_X, PLOT_MAX_X, PLOT_POINTS)
y_vals_base_expr, y_vals_taylor_expr = lam_base_expr(x_vals), lam_taylor_expr(x_vals)

# create subplot
fig, ax = plt.subplots()
# plot graphs
ax.plot(x_vals, y_vals_base_expr, label='f(x)')
ax.plot(x_vals, y_vals_taylor_expr, label=f'T({GRADE}, {DEVELOPMENT_POINT})(x)')
# styling (x and y axis, etc.)
ax.grid(True, which='both')

if PLOT_MIN_X < 0 < PLOT_MAX_X:
    ax.axvline(x=0, color='k')
if DRAW_X_AXIS:
    ax.axhline(y=0, color='k')
# set labels, enable legend and show
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
