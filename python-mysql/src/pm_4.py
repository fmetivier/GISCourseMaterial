# -*- coding: utf-8 -*-
"""
pm_4.py

same as pm_2.py but the data retrieval uses the OpenDB class 
"""

# import statements
import MySQLdb # MySQL api 
from matplotlib.pylab import *
from openDB import *


#get the data
#establish the connection
o=OpenDB(base="Parcelle",host="localhost",user="root",passwd="root")
#write and execute the query
sql="select date(date), sum(precip)  from imetos group by date(date)"
rows=o.execQuery(sql)

# define the variables as an empty python list
da=[]
pr=[]
# for each record returned store the values
for row in rows:
	da.append(row[0])
	pr.append(row[1])
	
# plot the results
fig=figure(1)
bar(da,pr)
xlabel('Date')
ylabel('Precipitation in mm')

fig.autofmt_xdate() # command to get the dates plotted correctly
show()

#close database
o.close()
