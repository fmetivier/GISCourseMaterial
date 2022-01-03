# -*- coding: utf-8 -*-
"""
pm_3.py

Python-Mysql DDL
"""
import MySQLdb

def create_connection(h = None, u = None, p = None):
	"""Creates and returns a connection object"""
	Conn = None
	if h is None or u is None or p is None:
		print("You must valid host, user and passwords")
	else:
		try:
			conn = MySQLdb.connect(host = h, user = u, passwd = p, charset = 'utf8', use_unicode = True)
		except:
			print("connection failed")
	return conn

def create_database(conn = None, dbname = None):
	"""
	Establish connection to MySQL
	Create database dbname
	"""
	if dbname is None or conn is None:
		print("You must provide a database name and valid connection")
		return
	else:
		# create base
		sql = "create database if not exists %s;" % dbname

		cursor = conn.cursor()
		res = cursor.execute(sql)
		print(res)
		conn.commit() # Needed in the case when you write something in the database.
		cursor.close()

def drop_database(conn = None, dbname = None):
    """
    Establish connection to MySQL
    drop database dbname
    """
    if dbname is None or conn is None:
        print("You must provide a database name and valid connection")
        return
    else:
		# drop base
        sql = "drop database %s;" % dbname
        cursor = conn.cursor()
        res = cursor.execute(sql)
        print(res)
        conn.commit() # Needed in the case when you write something in the database.
        cursor.close()

def sql(conn = None, dbname = None, sqlstatement = None):
    """
    executes an sql statement (other than select) in database dbname
    """
    if dbname is None or conn is None or sqlstatement is None:
        print("You must provide a database name and valid connection and sql statement")
        return
    else:
        # create a cursor object to send quaries
        cursor = conn.cursor()
        # connect to the database
        cursor.execute("use %s;" % (dbname))
        conn.commit()
        # execute de query
        cursor.execute(sqlstatement)
        conn.commit()
        cursor.close()

    return conn
