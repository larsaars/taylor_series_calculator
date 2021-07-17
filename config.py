from sympy import *

x = symbols('x')

# taylor series settings
DEVELOPMENT_POINT = 0
GRADE = 4
BASE_EXPR = sin(x)

# plot settings
PLOT_MIN_X, PLOT_MAX_X = -100, 100
PLOT_POINTS = abs(PLOT_MIN_X - PLOT_MAX_X) * 2
