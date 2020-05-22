#!/usr/local/bin/python
# coding: utf-8
# web,  os and db
"""
openDB.py

Class OpenDB: wrapper to connect and execute SQL queries (DDL and DML)
"""
import operator,  os,  pickle,  sys
import MySQLdb


class OpenDB:
    """
     class to encapsulate creation of connection and query execution to a Mysql Database
    """
    def __init__(self, base = None, user = None, passwd = None, host = None):
        if base is None or user is None or passwd is None or host is None:
            print("you must provide a valid database,  host,  user and password to create an OpenDB instance")
            return 1
        else:
            self.conn = MySQLdb.connect(host, user, passwd, base)

    def execQuery(self, req, param = ()):
        cursor = self.conn.cursor()
        try:
            cursor.execute(req, param)
        except Exception as err:
            # send back the message
            msg = "Incorrect SQL Query    : \n%s\nError detected:"%(req)    
            return msg+str(err)
        res = []
        if "SELECT" in req.upper():
            res =  cursor.fetchall()
        else:
            self.conn.commit()
        cursor.close()
        return res

    def QueryToFile(self, req, fname = 'out.txt', param = ()):
        """
        Executes a query and outputs to a text file for further processing (if needed)
        """
        res = self.execQuery(req, param)
        f = open(fname, 'w')
        for r in res:
            for i in npy.arange(len(r)-1):
                st = "%s\t" % (r[i])
                f.write(st)
            st = "%s\n" % (r[len(r)-1])            
            f.write(st)

        f.close()

    def close(self):
        self.conn.close()
