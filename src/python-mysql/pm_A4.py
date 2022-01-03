# -*- coding: utf-8 -*-
"""
pm_A4.py

Drawing Circle
"""


import matplotlib.pyplot as plt
import matplotlib.patches as pch
import matplotlib.collections as col
from matplotlib.lines import Line2D

def first():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Create the circle
    c = plt.Circle([25, 25], radius = 10, fc = 'r', ec = 'k', alpha = 0.5)
    #add it to the figure
    ax.add_artist(c)

    # Set axis form
    ax.axis('square')
    # Fix the limits. Axes will not know the limits from the Circle instance
    ax.set_ylim(0, 50)
    ax.set_xlim(0, 50)

    # Tricky Legend. Add a handle because legend can not get labels from a Circle (or a Rectangle or a Polygon)
    hd = [Line2D([0], [0], marker = 'o', markersize = 14, markerfacecolor = 'r', markeredgecolor = 'k', lw = 0, alpha = 0.5)]
    ax.legend(hd, ['A red circle'])

    # Save and show
    # plt.savefig("../figures/Circle.pdf", bbox_inches = 'tight')
    plt.show()

def second():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Create the red circles
    circles = []
    for i in range(10):
        c = pch.Circle([4*i,2*i], radius = 0.5*(i+1))
        circles.append(c) # add the circle to a list of circles
    # Create a collection of circles
    ccol = col.PatchCollection(circles, edgecolor = 'k', facecolor = 'r', alpha = 0.5, label = 'red')
    # Add them to the figure
    ax.add_collection(ccol)

    # s=Same for the green circles
    circles = []
    for i in range(10):
        c = pch.Circle([2*i,4*i], radius = (i+1))
        circles.append(c)
    ccol = col.PatchCollection(circles, edgecolor = 'k', facecolor = 'g', alpha = 0.5, label = 'green')
    ax.add_collection(ccol)

    # Set the axis.
    ax.axis('square')
    ax.set_ylim(0,50)
    ax.set_xlim(0,50)

    # Tricky legend
    # Create the handles using a Line2D object
    hd = [Line2D([0], [0], marker = 'o', markersize = 14, markerfacecolor = 'r', markeredgecolor = 'k', lw = 0, alpha = 0.5), Line2D([0],[0], marker = 'o', markersize = 14, markerfacecolor = 'g', markeredgecolor = 'k', lw = 0,alpha = 0.5)]
    # Create the legend calling the handles and adding labels.
    ax.legend(hd, ['Red circles','Green circles'], labelspacing = 1.2)

    # Save and show
    # plt.savefig('../figures/Circles.pdf', bbox_inches = 'tight')
    plt.show()

second()
