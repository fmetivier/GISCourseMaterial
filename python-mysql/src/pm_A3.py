# -*- coding: utf-8 -*-
"""
pm_A3.py

Using axes
"""

#import needed libraries
import  matplotlib.pylab as py

def xcosx():
    #define the data
    x = py.linspace(0, 10, 100)
    y = x*py.cos(x)
    y2 = x*py.sin(x)
    #plot the result
    fig = py.figure() #define the figure
    ax = fig.add_subplot(211) #create the axes and add a subplot
    ax2 = fig.add_subplot(212)
    ax.plot(x, y, 'r-') #make the plot
    ax2.plot(x, y2, 'g-')
    ax.set_xlabel('x', fontsize = 14) #add labels
    ax.set_ylabel('y', fontsize = 14)
    ax.legend(["$y = x \cos(x)$"], loc = "upper left") # add legend including LaTeX commands
    ax2.legend(["$y = x \sin(x)$"], loc = "upper left") # add legend including LaTeX commands
    py.show()



def two_axes():
    #define the data
    x = py.linspace(0, 100, 1000)
    y = py.cos(x)
    z = x**2
    #plot the results
    fig2 = py.figure() #define the figure
    ax21 = fig2.add_subplot(111) #create the axes and add a subplot
    ax22 = ax21.twinx() # create a new y-axis but keep the same x-axis
    ax21.plot(x, y, 'r-', label = '$y = \cos(x)$') #make the plot
    ax22.semilogy(x, z, 'g-', label = "$y = x^2$")
    ax21.set_xlabel('x', fontsize = 14) #add labels
    ax21.set_ylabel('y', color = 'r', fontsize = 14)
    ax22.set_ylabel('z', color = 'g', fontsize = 14)
    ax21.legend(loc = "upper left") # add legend including LaTeX commands
    ax22.legend(loc = "lower right")
    py.show() # show the figure

two_axes()
