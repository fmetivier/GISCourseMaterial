# -*- coding: utf-8 -*-
"""
pm_5.py

Plot of the hourly temperatures at Saint-Maur averaged over july,August and september
"""
#import libraries
import matplotlib.pylab as py
import openDB as odb

#get the data
#get your connection identifiers
f=open('./identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')

#establish the connection
o = odb.OpenDB(base = "Parcelle", user = mylogin, passwd = mypass, host = "localhost")
#write and execute the query
sql = "select hour(date), avg(tairav) from imetos  where month(date) in (7,8,9) group by hour(date)"
res = py.array(o.execQuery(sql))
o.close()

#retrieve the results
h = res.transpose()[0]
ta = res.transpose()[1]

#plot the result
fig = py.figure()
py.plot(h, ta, 'ro-')
py.xlabel("Hour of the day", fontsize = 14)
py.ylabel('Average temperature $^oC$', fontsize = 14)
py.axis([0, 24, 10, 25 ])
py.grid(True)

py.show()
