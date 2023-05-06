import numpy as np
import sys
from scipy import interpolate
from numpy.linalg import *
import sys
import math
import pandas as pd
import matplotlib.pyplot as plt

def read_by_tokens(fileobj):
    for line in fileobj:
        for token in line.split():
            yield token


f = open('inter_input.txt','r')

tokenized = read_by_tokens(f)

n = int(next(tokenized))

x=np.zeros(n)
y=np.zeros(n)
for i in range(n):
    x[i]=float(next(tokenized))
    y[i]=float(next(tokenized))

#print(x)
#print(y)

m=int(next(tokenized))
x_test=np.zeros(m)
for i in range(m):
    x_test[i]=float(next(tokenized))

def cubic_interpolate(x0, x, y):
    # Natural cubic spline interpolate function

    xdiff = np.diff(x)
    dydx = np.diff(y)
    dydx /= xdiff

    n = size = len(x)

    w = np.empty(n-1, float)
    z = np.empty(n, float)

    w[0] = 0.
    z[0] = 0.
    for i in range(1, n-1):
        m = xdiff[i-1] * (2 - w[i-1]) + 2 * xdiff[i]
        w[i] = xdiff[i] / m
        z[i] = (6*(dydx[i] - dydx[i-1]) - xdiff[i-1]*z[i-1]) / m
    z[-1] = 0.

    for i in range(n-2, -1, -1):
        z[i] = z[i] - w[i]*z[i+1]

    # find index (it requires x0 is already sorted)
    index = x.searchsorted(x0)
    np.clip(index, 1, size-1, index)

    xi1, xi0 = x[index], x[index-1]
    yi1, yi0 = y[index], y[index-1]
    zi1, zi0 = z[index], z[index-1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0/(6*hi1)*(xi1-x0)**3 + \
        zi1/(6*hi1)*(x0-xi0)**3 + \
        (yi1/hi1 - zi1*hi1/6)*(x0-xi0) + \
        (yi0/hi1 - zi0*hi1/6)*(xi1-x0)
    return f0
##################################################################################################
def lagrangepol(x0,x,y):
    yp = 0

    # Implementing Lagrange Interpolation
    for i in range(n):

        p = 1

        for j in range(n):
            if i != j:
                p = p * (x0 - x[j]) / (x[i] - x[j])

        yp = yp + p * y[i]
    return yp
#################################################################################

x_new = np.linspace(min(x), max(x), 10000)
plt.scatter(x, y, color='black', label='Data')
o = open('inter_output.txt', 'a')
ch = int(input("1.Cubic Spline\n2.Lagrange"))
if ch==1:
    y_new = cubic_interpolate(x_new, x, y)
    y_test = cubic_interpolate(x_test, x, y)
    o.write("\nCUBIC SPLINE INTERPOLATION\n")
    for i in range(m):
        o.write(f'{x_test[i]:.4f}' + "\t\t" + f'{y_test[i]:.4f}' + "\n")
    plt.plot(x_new, y_new, color='yellowgreen', label='Spline')
if ch==2:
        y_new2 = lagrangepol(x_new,x,y)
        y_test2=lagrangepol(x_test,x,y)
        o.write("LAGRANGE INTERPOLATION\n")
        for i in range(m):
            o.write(f'{x_test[i]:.4f}'+"\t\t"+f'{y_test2[i]:.4f}'+"\n")
        plt.plot(x_new, y_new2,color='blue',label='Lagrange')
plt.grid(axis='y')
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.legend()
plt.show()
o.close()
f.close()
