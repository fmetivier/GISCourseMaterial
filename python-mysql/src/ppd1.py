

import matplotlib.pyplot as plt
import MySQLdb as msql
import numpy as np

connection = msql.connect(host="localhost", user="root", passwd="iznogod01", db="Parcelle")
curseur =  connection.cursor()

sql="""select Nheures, count(*) as Njours
	from (select date(date) as  jour, count(*) as Nheures
		from imetos
		where precip>0
		group by date(date)) as R1
	group by Nheures """

curseur.execute(sql)
res=np.array(curseur.fetchall())
Nheures = res.transpose()[0]
Njours = res.transpose()[1]

plt.figure()
plt.plot(Nheures,Njours)
plt.show()
