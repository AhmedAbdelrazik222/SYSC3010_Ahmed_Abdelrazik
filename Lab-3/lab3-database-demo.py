#!/usr/bin/env python3
import sqlite3

#connect to database file
dbconnect = sqlite3.connect("lab4.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#Creating table and filling it
cursor.execute('CREATE TABLE sensors (sensorID NUMERIC, type TEXT, zone TEXT);')

cursor.execute('''INSERT INTO sensors values(1, "door", "kitchen");''')
cursor.execute('''INSERT INTO sensors values(2, "temperature", "kitchen");''')
cursor.execute('''INSERT INTO sensors values(3, "door", "garage");''')
cursor.execute('''INSERT INTO sensors values(4, "motion", "garage");''')
cursor.execute('''INSERT INTO sensors values(5, "temperature", "garage");''')

dbconnect.commit();
#Printing the desired sensors
cursor.execute('SELECT * FROM sensors')
for row in cursor:
    if row['zone'] == "kitchen" or row['type']=="door":
        print('ID: ',row['sensorID'],', type: ',row['type'],', zone: ', row['zone']);
dbconnect.close()