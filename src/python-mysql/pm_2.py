"""
pm_2.py

 a simple Python script that
 1) connects to the Parcelle database
 2) queries the imetos table for daily precipitations
 3) plots the retrieved data
"""


# import statements
import MySQLdb # MySQL api
import matplotlib.pylab as py


#get your connection identifiers
f=open('./identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')

# name of the database you whish to connect to
base = 'Parcelle'
# establish connection
conn = MySQLdb.connect(host="localhost", user=mylogin, passwd=mypass, db=base)
# create a cursor object to send quaries
cursor = conn.cursor()
# write the SQL query
query = 'select date(date), sum(precip) from imetos group by date(date)'
# execute the query
cursor.execute(query)
# fetch the dataset
rows = cursor.fetchall()

# define the variables as an empty python list
da = []
pr = []
# for each record returned store the values
for row in rows:
	da.append(row[0])
	pr.append(row[1])

# plot the results
fig = py.figure(1)
py.bar(da,pr)
py.xlabel('Date')
py.ylabel('Precipitation in mm')

fig.autofmt_xdate() # command to get the dates plotted correctly
#py.savefig("../figures/pm_2.pdf", bbox_inches = 'tight')
py.show()

cursor.close()
conn.close()
