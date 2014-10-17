from collections import defaultdict
import csv
import sqlite3


#csv example

headers = ( 'first_name', 'last_name', 'company', 'address', 'city', 'county', 'state', 'zip', 'phone1', 'phone2', 'email', 'web')
grouped_header = collections.namedtuple(Headers)
for emp in map(Headers._make, csv.reader(open("us-500.csv", "rU"))):
    print emp.first_name, emp.phone1



# sqlite3 example
conn = sqlite3.connect('/customerlist')
cursor = conn.cursor()
cursor.execute('SELECT first_name, last_name, company, address, city, county, state, zip, phone1, phone2, email, web FROM customer')
for emp in map(Headers._make, cursor.fetchall()):
    print emp.first_name, emp.phone1