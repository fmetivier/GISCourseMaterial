# -*- coding: utf-8 -*-
"""
pm_A5.py

Different ways to build a legend
"""
#import needed libraries
import matplotlib.pylab as py
from matplotlib.lines import Line2D
import numpy as np

def leg_1():
	
	"""Adding labels"""
	
	# Define the data
	x = py.linspace(0, 10, 100) 
	y = x * py.cos(x)
	z = x * py.sin(x)

	py.figure() #define the figure
	py.plot(x, y, 'r-', label = '$x\cos(x)$') #LABELS PLACED INSIDE THE PLOT COMMANDS
	py.plot(x, z, 'g-', label = '$x\sin(x)$')

	py.xlabel('x', fontsize = 14) #add labels
	py.ylabel('y', fontsize = 14)

	#LEGEND CALL
	py.legend(loc = "upper left") # add legend including LaTeX commands

	py.show() # show the figure

def leg_2():
	
	"""Adding labels second version"""
	
	# Define the data
	x = py.linspace(0, 10, 100) 
	y = x*py.cos(x)
	z = x*py.sin(x)

	py.figure() # Define the figure
	py.plot(x, y, 'r-') 
	py.plot(x, z, 'g-')

	py.xlabel('x', fontsize = 14) # Add labels
	py.ylabel('y', fontsize = 14)

	# LEGEND CALL
	py.legend(labels = ['$x\cos(x)$', '$x\sin(x)$'], loc = "lower left") # add legend including LaTeX commands

	py.show() # Show the figure

def leg_3():
	
	"""Retrieving axes,  handles and labels"""
	
	# Define the data
	x = py.linspace(0, 10, 100) 
	y = x * py.cos(x)
	z = x * py.sin(x)

	fig = py.figure() #define the figure
	ax = fig.add_subplot(111)
	ax.plot(x, y, 'r-', label = '$x\cos(x)$') 
	ax.plot(x, z, 'g-', label = '$x\sin(x)$')

	py.xlabel('x', fontsize = 14) #add labels
	py.ylabel('y', fontsize = 14)

	# LEGEND CALL
	handles, labels = ax.get_legend_handles_labels()
	py.legend(handles, labels, bbox_to_anchor = (0.5, 1.1), ncol = 2, loc = 'center') # add legend including LaTeX commands

	py.show() # show the figure

def leg_4():
	
	"""Phantom legend: very useful to represent collections and group labels"""
	
	fig = py.figure() #define the figure
	ax = fig.add_subplot(111)
	
	# Create a phantom plot
	for i in range(4): 
		py.scatter([],  [],  s = np.exp(i+1),  edgecolor = 'k', facecolor = 'none', label = str(i+1))

	# Get the legend handles andlabels
	h,  l  =  py.gca().get_legend_handles_labels()
	# Add a new handle and label
	h.append(Line2D([0], [0], color = 'r',  lw = 3))
	l.append('a red line !')
	
	ax.legend(h,  l, title = "Phantoms", labelspacing = 2, borderpad = 2, frameon = True,  ncol = 5, loc = 2)

	py.show()
	

