from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory
import sys
import csv
import pandas as pd
auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster()
cluster = Cluster(['172.19.0.3', '172.19.0.4', '172.19.0.5', '172.19.0.5'], port=9042, auth_provider=auth_provider)
session = cluster.connect('keyspace')
session.row_factory = dict_factory
rows = session.execute('SELECT *  FROM YourTableName')
dataframe = pd.DataFrame(rows)
dataframe.to_csv('YourTableName.csv')

# print only one row
#print (rows[0]) 

print (dataframe) # print full table
#for row in df:
#    print (row[])


