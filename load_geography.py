# -*- coding: utf-8 -*-
import pyodbc
import csv
server = "lds.di.unipi.it"
database = "Group_3_DB"
username = "Group_3"
password = "GN3RTNTX"
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password


sql = "INSERT INTO Geography (country_ioc,continent,language) VALUES (?,?,?)"

file_geography = open("output/geography.csv", mode='r')
csv_file = csv.DictReader(file_geography, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val = (line["country_ioc"], line["continent"], line["language"])
    cursor.execute(sql, val)
    print("Inserisco riga %d" % i)
    i = i + 1

file_geography.close()
cnxn.commit()
cursor.close()
cnxn.close()

