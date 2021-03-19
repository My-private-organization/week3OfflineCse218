import matplotlib.pyplot as plotter
import numpy as num
from function import my_function

x = num.linspace(0, .999999, 1000)

plotter.plot(x, my_function(x))

plotter.xlabel('x - axis')
plotter.ylabel('y - axis')

plotter.axhline(0, color='#000000')
plotter.axvline(0, color='#000000')

plotter.xlim(0, 1)
plotter.ylim(0, 300)

plotter.show()

