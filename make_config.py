"""
execute this to input function and other config by hand over terminal
"""

from taylor_calculator_and_plotter import *

BASE_EXPR = sympify(input('f(x) = ') or 'cos(x)')
DEVELOPMENT_POINT = float(input('development point [0]: ') or '0')
GRADE = int(input('grade [4]: ') or '4')
PLOT_RANGE = int(input('plot range [3]: ') or '3')

calculate_and_plot()
