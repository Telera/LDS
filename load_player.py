# -*- coding: utf-8 -*-
import pyodbc
import csv

server = "lds.di.unipi.it"
database = "Group_3_DB"
username = "Group_3"
password = "GN3RTNTX"
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password

sql = "INSERT INTO Player (player_id,country_id,name,sex,hand,year_of_birth) VALUES (?,?,?,?,?,?)"

file_player = open("output/player.csv", mode='r')
csv_file = csv.DictReader(file_player, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val = (line["player_id"], line["country_id"], line["name"], line["sex"], line["hand"], line["year_of_birth"])
    cursor.execute(sql, val)
    if i % 50 == 0:
        print("Inserted row %d" % i)
    i = i + 1

file_player.close()
cnxn.commit()
cursor.close()
cnxn.close()
