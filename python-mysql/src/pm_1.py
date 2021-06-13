# -*- coding: utf-8 -*-
"""
pm_1.py

First Python-Mysql script
"""
import matplotlib.pylab as py
import MySQLdb as msql

#get your connection identifiers
f=open('./identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')

# 1) Create connection
conn = msql.connect(host="localhost", user=mylogin, db="Parcours", passwd=mypass)

# 2) Create postman (cursor)
postman = conn.cursor()

# 3) write SQL GEI
sql="select anneeUFR, count(*) from IdentiteTbl where anneeUFR>1900 and type='GEI' group by anneeUFR"

# 4) Send letter
postman.execute(sql)

# 5) Receive answer
res=py.array(postman.fetchall())

# 6) Process
anneeGEI=res.transpose()[0]
inscritsGEI=res.transpose()[1]

# graphique
fig=py.figure()
py.bar(anneeGEI, inscritsGEI, color = 'lightgreen')
py.ylabel(u"Number of registered students")
py.xlabel(u"Year of enrollment")
#py.savefig("../figures/FigSQL1.pdf", bbox_inches = 'tight')
py.show()

# close the connexion
postman.close()
conn.close()
