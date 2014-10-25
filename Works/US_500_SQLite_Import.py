__author__ = 'INKQWIRE'

import os, csv, json, re
import sqlite3


conn = sqlite3.connect('US_500.sqlite')
conn.text_factory = str
cursor = conn.cursor()
reader = cursor.execute ("SELECT phone1 FROM SampleData where phone1 LIKE '%%' GROUP BY substr(phone1, 5) ")
# reader = cursor.execute ("SELECT phone1 FROM SampleData where phone1 LIKE '________%' ORDER BY phone1 desc")

tabledata = cursor.fetchall()
for row in (tabledata):
	print str(row)

conn.close()

# tabledata=[[str[row] for row in tabledata] for tabledata in cursor.fetchall()]
# print tabledata

# for row in (tabledata):
# 	print str(row)

# for row in cursor:
#     print str(row)

# conn.row_factory = sqlite3.Row
#
# tables = ['SampleData'];
# for table in tables:
#     rows = conn.execute("SELECT first_name FROM SampleData);
#     for row in rows:
#         IDs.append( (row['phone1'],table) )