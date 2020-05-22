# -*- coding: utf-8 -*-
"""
pm_4p.py

same as pm_2.py and pm_4.py but the data retrieval uses SQLAlchemy and Pandas
instead of MySQLdb
"""

# import statements
import matplotlib.pylab as py
from sqlalchemy import create_engine
import pandas

# default syntax engine = create_engine('mysql://user:passwd@host/dbname')
engine = create_engine('mysql://root:iznogod01@localhost/Parcelle')

sql = "select date(date) as d, sum(precip) as p  from imetos group by date(date)"
df = pandas.read_sql(sql, engine)

	
# plot the results
fig=py.figure(1)
py.bar(df['d'], df['p'])
py.xlabel('Date')
py.ylabel('Precipitation in mm')

fig.autofmt_xdate() # command to get the dates plotted correctly
py.show()

engine.close()
