# -*- coding: utf-8 -*-
import pyodbc
import csv

server = "lds.di.unipi.it"
database = "Group_3_DB"
username = "Group_3"
password = "GN3RTNTX"
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

sql = "INSERT INTO Tournament (tourney_id,date_id,tourney_name,surface,draw_size,tourney_level,tourney_spectators,tourney_revenue) VALUES (?,?,?,?,?,?,?,?)"

file_tournament = open("output/tournament.csv", mode='r')
csv_file = csv.DictReader(file_tournament, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val = (line["tourney_id"], line["date_id"], line["tourney_name"], line["surface"], line["draw_size"], line["tourney_level"], line["tourney_spectators"], line["tourney_revenue"])
    cursor.execute(sql, val)
    if i % 50 == 0:
        print("Inserted row %d" % i)
    i = i + 1

file_tournament.close()
cnxn.commit()
cursor.close()
cnxn.close()
