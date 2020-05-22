# -*- coding: utf-8 -*-
"""
pm_A2.py

Solution of a steady 1D flow using Dupuit approximation over a length L
for different values of hydraulic conductivity K 
Boundary conditions are a flux  Q at 0 and zero depth y at 1.
"""
# Import libraries
import matplotlib.pylab as py

# Define the problem
# constants
L = 0.8 # "true" length 
Q = 1./6000 # discharge m2/s
K = [0.1, 0.075, 0.05, 0.025, 0.01] # hydraulic conductivity

# variable
x = py.linspace(0, L, 100) # x value array

# Prepare the figure
py.figure()
lgd=[] #legend

for k in K:
    y = py.sqrt((2*Q/k)*(L-x)) # analytic solution for the water thickness
    st = "$ K=%s $" % (k) # add the conductivity to the legend
    lgd.append(st)
    py.plot(x, y)     #plot the result

# Figure labels, legend and axis
py.xlabel('x', fontsize = 14)
py.ylabel('$h=\sqrt{(2q/K)(L-x)}$',fontsize=14)
py.legend(lgd, loc = "upper right") # including LaTeX labels
py.axis([0, 0.8, 0, 0.2])

# save and display
py.savefig("../figures/pm_A2.pdf", bbox_inches = 'tight')
py.show()
