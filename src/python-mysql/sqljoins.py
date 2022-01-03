#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
sqljoins.py

Different types of SQL joins using shapely and matplotlib
"""
import shapely.geometry as sg
import shapely.ops as so
import matplotlib.pyplot as plt

#constructing the first rect as a polygon
r1 = sg.Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])

#a shortcut for constructing a rectangular polygon
r2 = sg.box(0.5, 0.5, 1.5, 1.5)

x1, y1 = r1.exterior.xy
x2, y2 = r2.exterior.xy

rows = 4
cols = 2

fig = plt.figure(figsize = (10, 20))

#Inner join
ns = r1.intersection(r2)
xs, ys = ns.exterior.xy

axs = fig.add_subplot(rows, cols, 1)
axs.plot(x1, y1, 'r-')
axs.plot(x2, y2, 'r-')
axs.fill(xs, ys, alpha = 0.5, fc = 'r', ec = 'none')
axs.text(0.1, 0.1, "A")
axs.text(1.4, 1.4, "B")
axs.set_title("Jointure interne")
axs.axis('off')


#Left join
axs = fig.add_subplot(rows, cols, 3)
axs.plot(x1, y1, 'r-')
axs.plot(x2, y2, 'r-')
axs.fill(x1, y1, alpha = 0.5, fc = 'r', ec = 'none')
axs.text(0.1, 0.1, "A")
axs.text(1.4, 1.4, "B")
axs.set_title(u"Jointure à gauche")
axs.axis('off')

#Left Outer join
nso = r1.symmetric_difference(r2)
left = nso[0]
xsl, ysl = left.exterior.xy

axs = fig.add_subplot(rows, cols, 4)
axs.plot(x1, y1, 'r-')
axs.plot(x2, y2, 'r-')
axs.fill(xsl, ysl, alpha = 0.5, fc = 'r', ec = 'none')
axs.text(0.1, 0.1, "A")
axs.text(1.4, 1.4, "B")
axs.set_title(u"J. à gauche sans intersection")
axs.axis('off')

#Right join
axs = fig.add_subplot(rows, cols, 5)
axs.plot(x1, y1, 'r-')
axs.plot(x2, y2, 'r-')
axs.fill(x2, y2, alpha = 0.5, fc = 'r', ec = 'none')
axs.text(0.1, 0.1, "A")
axs.text(1.4, 1.4, "B")
axs.set_title(u"Jointure à droite")
axs.axis('off')

#Right Outer join
right = nso[1]
xsr, ysr = right.exterior.xy

axs = fig.add_subplot(rows, cols, 6)
axs.plot(x1, y1, 'r-')
axs.plot(x2, y2, 'r-')
axs.fill(xsr, ysr, alpha = 0.5, fc = 'r', ec = 'none')
axs.text(0.1, 0.1, "A")
axs.text(1.4, 1.4, "B")
axs.set_title(u"J. à droite sans intersection")
axs.axis('off')

#Full join
ns = so.cascaded_union([r1, r2])
xs, ys = ns.exterior.xy

axs = fig.add_subplot(rows, cols, 7)
axs.plot(x1, y1, 'r-')
axs.plot(x2, y2, 'r-')
axs.fill(xs, ys, alpha = 0.5, fc = 'r', ec = 'none')
axs.text(0.1, 0.1, "A")
axs.text(1.4, 1.4, "B")
axs.set_title("Jointure externe")
axs.axis('off')


#Full outer join
axs = fig.add_subplot(rows, cols, 8)
axs.plot(x1, y1, 'r-')
axs.plot(x2, y2, 'r-')
axs.fill(xsl, ysl, alpha = 0.5, fc = 'r', ec = 'none')
axs.fill(xsr, ysr, alpha = 0.5, fc = 'r', ec = 'none')
axs.text(0.1, 0.1, "A")
axs.text(1.4, 1.4, "B")
axs.set_title("J. externe sans intersection")
axs.axis('off')

# plt.savefig("../figures/SQL_joins.pdf", bbox_inches = 'tight')
plt.show() #if not interactive
