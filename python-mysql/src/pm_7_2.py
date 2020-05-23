"""
pm_7_2.py

use pandas to read sql data from Mysql database using a SELECT query
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

sql="select year(date) as y, month(date) as m, sum(precip) as pcum from imetos group by month(date),year(date) order by year(date),month(date)"

df = pandas.read_sql(sql,engine)
print(df.head())
