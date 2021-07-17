from sympy import *

x = symbols('x')

# taylor series settings
DEVELOPMENT_POINT = 8
GRADE = 4
BASE_EXPR = cos(x)

# plot settings
PLOT_MIN_X, PLOT_MAX_X = 5, 12
PLOT_POINTS = 1000
