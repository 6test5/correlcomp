'''
Correlation func
Created on 29.06.2019
@author: /dat
'''

import numpy as np
import matplotlib.pyplot as plt
import cmath
import math
from itertools import groupby

fixed_row_Xr_Xi = [-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


Yr = [-10, -9.5, -9, -8.5, -8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5, -3, -2.5, -2, -1.5, -1, -0.5,
      0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]

# Yi = [2, 5.122498999, 6.358898944, 7.267826876, 8, 8.614378278, 9.141428429, 9.599342077, 10,
#       10.35164654, 10.66025404, 10.93028555, 11.16515139, 11.367497, 11.53939201, 11.68245837, 11.79795897,
#       11.88685997, 11.94987437, 11.98749218, 12, 11.98749218, 11.94987437, 11.88685997, 11.79795897, 11.68245837,
#       11.53939201, 11.367497, 11.16515139, 10.93028555, 10.66025404, 10.35164654, 10, 9.599342077, 9.141428429,
#       8.614378278, 8, 7.267826876, 6.358898944, 5.122498999, 2]

# Y_avg = np.average(Yi)
overall = []
gc = 0


def complexcorrel_linear(xs, ys, y2s):
    x_complex = []
    y_complex = []
    x_powered_sum = 0
    y_powered_sum = 0
    yx_sum = 0

    for x, y, y2 in zip(xs, ys, y2s):  # To complex
        comp = complex(x, x)
        x_complex.append(comp)
        yi_avg = y2 - Y_avg
        comp = complex(y, yi_avg)
        y_complex.append(comp)
    for x, y in zip(x_complex, y_complex):  # To YX
        yx = np.multiply(x, y)
        yx_sum += yx
        x2 = (abs(x))**2 * (math.cos(2*(cmath.phase(x))) + math.sin(2*cmath.phase(x))*1j)
        x_powered_sum += x2
        y2 = (abs(y))**2 * (math.cos(2*(cmath.phase(y))) + math.sin(2*cmath.phase(y))*1j)
        y_powered_sum += y2
    sqrt_sumx_sumy = cmath.sqrt((x_powered_sum * y_powered_sum))
    correl = yx_sum/sqrt_sumx_sumy
    overall.append(correl)
    # return correl


# def graph(x, y):
#     plt.plot(x, y)
#     plt.ylabel('Wow')
#     plt.show()


for a_s in np.arange(-10, 10, 0.5):   # линейная
    gc += 1
    for x_s in np.arange(-10, 10, 0.5):
        Yi = []
        for b_s in np.arange(-10, 10, 0.5):
            y = a_s * x_s + b_s
            Yi.append(y)
        else:
            Y_avg = np.average(Yi)
            complexcorrel_linear(fixed_row_Xr_Xi, Yr, Yi)
            # graph(Yr, Yi)

if gc == 40:
    new_overall = [el for el, _ in groupby(overall)]
    print(new_overall)
