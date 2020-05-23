# -*- coding: utf-8 -*-
"""
pm_3-1.py

Python-Mysql DDL exemples using the library pm3
"""

import pm_3

#get your connection identifiers
f=open('./identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')

#creates connection
myconn = pm_3.create_connection(h = "localhost", u = mylogin, p = mypass)

#creates database
pm_3.create_database(myconn,"Toto")

#
#sql queries
#

#create table
pm_3.sql(conn = myconn, dbname = "Toto", sqlstatement = "create table if not exists tata (val1 int, val2 int, val3 float)")

#insert data
query = "insert into tata values (1,2,3.0),(2,3,4.0),(3,4,5.0)"

pm_3.sql(conn = myconn, dbname = "Toto", sqlstatement = query)

# close connection
myconn.close()
