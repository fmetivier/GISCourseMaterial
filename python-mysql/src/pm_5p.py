# -*- coding: utf-8 -*-
"""
pm_5p.py

same as pm_5.py but with SQLAlchemy and Pandas
"""

#import libraries
import matplotlib
matplotlib.use('GTKAgg')

import matplotlib.pylab as py
from sqlalchemy import create_engine
import pandas

# default syntax engine = create_engine('mysql://user:passwd@host/dbname')
engine = create_engine('mysql://root:iznogod01@localhost/Parcelle')

#get the data
sql = "select hour(date) as h, avg(tairav) as ta from imetos  where month(date) in (7,8,9) group by hour(date)"
df = pandas.read_sql(sql, engine)



#plot the result
fig=py.figure()
py.plot(df['h'], df['ta'], 'ro-')
py.xlabel("Hour of the day", fontsize = 14)
py.ylabel('Average temperature $^oC$', fontsize = 14)
py.axis([0, 24, 10, 25 ])
py.grid(True)
py.show()

engine.close()