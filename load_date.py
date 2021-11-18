# -*- coding: utf-8 -*-
import pyodbc
import csv

server = "lds.di.unipi.it"
database = "Group_3_DB"
username = "Group_3"
password = "GN3RTNTX"
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

sql = "INSERT INTO Date (date_id,day,month,year,quarter) VALUES (?,?,?,?,?)"

file_date = open("output/date.csv", mode='r')
csv_file = csv.DictReader(file_date, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

for line in csv_file:
    val = (line["date_id"], line["day"], line["month"], line["year"], line["quarter"])
    cursor.execute(sql, val)
print("Rows inserted successfully!")


file_date.close()
cnxn.commit()
cursor.close()
cnxn.close()
