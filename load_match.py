# -*- coding: utf-8 -*-
import pyodbc
import csv

server = "lds.di.unipi.it"
database = "Group_3_DB"
username = "Group_3"
password = "GN3RTNTX"
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password
sql = "INSERT INTO Match (tourney_id, match_id, winner_id, loser_id, score, best_of, round, minutes, w_ace, w_df, w_svpt, w_1stIn, w_1stWon, w_2ndWon, w_SvGms, w_bpSaved, w_bpFaced, l_ace, l_df, l_svpt,l_1stIn, l_1stWon, l_2ndWon, l_SvGms, l_bpSaved, l_bpFaced) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

file_match = open("output/match.csv", mode='r', encoding='utf-8-sig')
csv_file = csv.DictReader(file_match, delimiter=",")

cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()
i = 1

for line in csv_file:
    val =(line["tourney_id"], line["match_id"], line["winner_id"], line["loser_id"], line["score"],
          line["best_of"], line["round"],line["minutes"],line["w_ace"],line["w_df"],line["w_svpt"], line["w_1stIn"],
          line["w_1stWon"],line["w_2ndWon"],line["w_SvGms"],line["w_bpSaved"],line["w_bpFaced"], line["l_ace"],
          line["l_df"],line["l_svpt"],line["l_1stIn"], line["l_1stWon"],line["l_2ndWon"],line["l_SvGms"],
          line["l_bpSaved"],line["l_bpFaced"],)
    cursor.execute(sql, val)
    if i % 500 == 0:
        print("Inserted row %d" % i)
    i = i + 1

file_match.close()
cnxn.commit()
cursor.close()
cnxn.close()




