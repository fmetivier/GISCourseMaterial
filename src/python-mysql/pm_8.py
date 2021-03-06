"""
pm_8.py

use pandas to read sql data from Mysql database and compare syntaxes
"""
#library needed to create a connection that pandas can use
from sqlalchemy import create_engine
# pandas
import pandas

#get your connection identifiers
f=open('./identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')

# default syntax engine = create_engine('mysql://user:passwd@host/dbname')
engine = create_engine('mysql://%s:%s@localhost/Parcelle' % (mylogin,mypass))
conn = engine.connect()
df = pandas.read_sql_table('imetos',conn)
print(df.head())


print("Number of hours of precipitation")
# select count(*) from imetos where precip > 0
print(df[df["precip"] > 0]["date"].count())


print("Number of hours of precipitation during night time")
# select count(*) from imetos where precip > 0 and solrad=0
print(df[(df["precip"] > 0) & (df["solrad"] == 0)]["date"].count())


print("Monthly Averaged hourly precipitation  during daytime")
# select month(date), avg(precip) from imetos where solrad >0 group by month(date)
print(df[df["solrad"] > 0].groupby(df["date"].dt.month)["precip"].mean())

#etc...
