"""
pm_9.py

use pandas to write pandas data to a MySQL table
"""
#library needed to create a connection that pandas can use
from sqlalchemy import create_engine
# pandas
import pandas
import numpy as np

# connect to the Toto db
engine = create_engine('mysql://login:password@localhost/Toto')

# create a dataframe with three series val1, val2 val3 of 100 000 values
# val 1 in [0,10]
val1 = np.random.randint(0,10,100000)
print(val1)
# val 2 in [0,100]
val2 = np.random.randint(0,100,100000)
print(val2)
# val 3 in [0,1000.0] uniform distribution
val3 = np.random.rand(100000)*1000.0
print(val3)

# create the frame
df = pandas.DataFrame({"val1": val1.tolist(), "val2": val2.tolist(),"val3": val3.tolist()})
print(df.head())

#store the data in table tata
df.to_sql('tata', engine, if_exists = 'append', index = False)
