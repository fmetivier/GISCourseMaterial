# -*- coding: utf-8 -*-
"""
pm_A1.py

plot xcos(x)
"""
#import needed libraries
import matplotlib.pylab as py

#define the data
x=py.linspace(0,10,100)
y=x*py.cos(x)

#plot the result
py.figure() #define the figure
py.plot(x,y,'r-') #make the plot
py.xlabel('x',fontsize=14) #add labels
py.ylabel('y',fontsize=14)
py.legend(["$y=x \cos(x)$"],loc="upper left") # add legend including LaTeX commands
# py.savefig("../figures/pm_A1.pdf",bbox_inches='tight') # save figure to file
py.show() # show the figure
