# -*- coding: utf-8 -*-
import pyodbc
import csv

server = "lds.di.unipi.it"
database = "Group_3_DB"
username = "Group_3"
password = "GN3RTNTX"
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
sql = "INSERT INTO Match (tourney_id, match_id, winner_id, loser_id, score, best_of, round, minutes, w_ace, w_df, w_svpt, w_1stWon, w_2ndWon, w_SvGms, w_bpSaved, w_bpFaced, l_ace, l_df, l_svpt, l_1stWon, l_2ndWon, l_SvGms, l_bpSaved, l_bpFaced) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

file_match = open("output/match.csv", mode='r', encoding='utf-8-sig')
csv_file = csv.DictReader(file_match, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val =(line["tourney_id"], line["match_id"], line["winner_id"], line["loser_id"], line["score"],
          line["best_of"], line["round"],line["minute"],line["w_ace"],line["w_df"],line["w_svpt"],
          line["w_1stWon"],line["w_2ndWon"],line["w_SvGm"],line["w_bpSaved"],line["w_bpFaced"], line["l_ace"],
          line["l_df"],line["l_svpt"], line["l_1stWon"],line["l_2ndWon"],line["l_SvGm"],
          line["l_bpSaved"],line["l_bpFaced"],)
    cursor.execute(sql, val)
    print("Inserisco riga %d" % i)
    i = i + 1

file_match.close()
cnxn.commit()
cursor.close()
cnxn.close()

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


sql = "INSERT INTO Player (player_id,country_id,name,sex,hand,year_of_birth) VALUES (?,?,?,?,?,?)"

file_player = open("output/player.csv", mode='r')
csv_file = csv.DictReader(file_player, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val = (line["player_id"], line["country_id"], line["name"], line["sex"], line["hand"], line["year_of_birth"])
    cursor.execute(sql, val)
    print("Inserisco riga %d" % i)
    i = i + 1

file_player.close()
cnxn.commit()
cursor.close()
cnxn.close()


sql = "INSERT INTO Tournament (tourney_id,date_id,tourney_name,surface,draw_size,tourney_level,turney_spectators,tourney_revenue) VALUES (?,?,?,?,?,?,?,?,?,?)"

file_tournament = open("output/player.csv", mode='r')
csv_file = csv.DictReader(file_tournament, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val = (line["tourney_id"], line["date_id"], line["tourney_name"], line["surface"], line["draw_size"], line["tourney_level"], line["tourney_spectators"], line["tourney_revenue"])
    cursor.execute(sql, val)
    print("Inserisco riga %d" % i)
    i = i + 1

file_tournament.close()
cnxn.commit()
cursor.close()
cnxn.close()



sql = "INSERT INTO Date (date_id,day,month,year,quarter) VALUES (?,?,?,?,?)"

file_date = open("output/date.csv", mode='r')
csv_file = csv.DictReader(file_date, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val = (line["date_id"], line["day"], line["month"], line["year"], line["quarter"])
    cursor.execute(sql, val)
    print("Inserisco riga %d" % i)
    i = i + 1

file_date.close()
cnxn.commit()
cursor.close()
cnxn.close()