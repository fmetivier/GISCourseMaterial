"""
sqla_1.py

use sqlalchemy to connect to a Mysql database
"""

from sqlalchemy import create_engine
f=open('./identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')

############################
#If python-mysql installed
############################
engine = create_engine('mysql://%s:%s@localhost/Parcelle' % (mylogin,mypass))
############################
#Else if pymysql installed
############################
#engine = create_engine('mysql+pymysql://%s:%s@localhost/Parcelle' % (mylogin,mypass))
############################
#Else if mysqlclient installed
############################
#engine = create_engine('mysql+mysqlclient://%s:%s@localhost/Parcelle' % (mylogin,mypass))

# establish connection
conn = engine.connect()

sql = "select * from imetos where precip > 0"
res = conn.execute(sql)

for row in res.fetchall():
    print( row )
