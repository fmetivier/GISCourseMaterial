"""
pm_7.py

use pandas to read an sql table from Mysql database
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

df = pandas.read_sql_table('imetos',engine)
print(df.head())
