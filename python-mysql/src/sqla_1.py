"""
sqla_1.py

use sqlalchemy to connect to a Mysql database
"""

from sqlalchemy import create_engine
mylogin="XXXX"
mypass="YYYY"

# default syntax engine = create_engine('mysql://user:passwd@host/dbname')
engine = create_engine('mysql://%s:%s@localhost/Parcelle' % (mylogin,mypass))
# establish connection
conn = engine.connect()

sql = "select * from imetos where precip > 0"
res = conn.execute(sql)
row = res.fetchone()

for row in res:
   print (row)
