# -*- coding: utf-8 -*-
"""
pm_6p.py

plots the histogram of wind directions at Saint-Maur as a polar plot. same as pm_6.py but here we use SQLAlchemy and Pandas to retrieve and process the data
"""
#import libraries
import matplotlib.pylab as py

from sqlalchemy import create_engine
import pandas

# default syntax engine = create_engine('mysql://user:passwd@host/dbname')
engine = create_engine('mysql://root:iznogod01@localhost/Parcelle')

sql="select round(winddir/20)*20 as theta, count(winddir) as radii from imetos group by round(winddir/20)*20 order by winddir" 
df = pandas.read_sql(sql,engine)

# add the values of 0 and 360 degrees together, put the values at 360 to 0
df.at[0, 'radii'] += df.at[18, 'radii']
df.at[18, 'radii'] = 0


# force square figure and square axes as it looks better for polar plots
fig = py.figure(figsize=(8,8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

width = 20.*py.pi/180.
bars = py.bar(df['theta']*py.pi/180, df['radii'], width=width, bottom=0.0)
for r,bar in zip(df['radii'].to_list(), bars):
    bar.set_facecolor("r")
    bar.set_edgecolor("k")
    bar.set_alpha(0.5)
 
py.show()
