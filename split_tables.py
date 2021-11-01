import csv
import re

"""
# tournament
date id <- da creare
0 1 2 3 4 47 48

# Player
WINNER 7  12 9  10 11
LOSER  14 19 16 17 18
Gender <- creare
byear of birth <- creare

# Match
0 
7  winner id
14 loser id
match id (match num+tourney id) <- creare
21 score
22-46 incluso
"""


def add_language(path):
    diz = {}
    with open(path, "r") as f:
        header = f.readline()
        tokens_header = header.strip().split(',')
        for ind, token in enumerate(tokens_header):
            if token == "country_name":
                ind_country = ind
            if token == "lang_name":
                ind_lang = ind
        first = True
        for line in f:
            if first:
                first = False
            else:
                tokens = line.strip().split(',')
                diz[tokens[ind_country]] = tokens[ind_lang]
        return(diz)

def geography_to_csv(path):
    with open(path, "r") as f:
        header = f.readline()
        tokens_header = header.strip().split(',')
        for ind, token in enumerate(tokens_header):
            if token == "country_code":
                ind_code = ind
            if token == "country_name":
                ind_country = ind
            if token == "continent":
                ind_continent = ind
        first = True
        file_continent = open("geography.csv", mode='a')
        file_continent.write("coutry_loc,continent,language")
        for line in f:
            if first:
                first = False
            else:
                tokens = line.strip().split(',')
                diz_language = add_language("data2021/country_list.csv")
                row = []
                row.append(tokens[ind_code])
                row.append(tokens[ind_continent])
                row.append(diz_language[tokens[ind_country]])
                print(row)
                #todo write row in the file

        file_continent.close()

def preprocessing_match(dict):
    print(dict["tourney_id"])
    tourney_name = dict["tourney_id"] + "-"
    print(tourney_name)
    num_tourney = re.search("-[M]*[0-9]+[A-Z]*-", tourney_name)

    print(dict["tourney_id"], "****", num_tourney.group(0))

#print(add_language("data2021/country_list.csv"))
#print(geography_to_csv("data2021/countries.csv"))

tennis_file = open("data2021/tennis.csv", "r")
reader = csv.DictReader(tennis_file)
header = reader.fieldnames
print(header)


headers = {}
headers["match"] = [header[0]] + header[6:8] + [header[14]] + header[21:47]
headers["tournament"] = header[0:5] + header[47:49]
headers["winner_player"] = [header[7]] + header[9:13]
headers["loser_player"] = [header[14]] + header[16:20]

print(headers)

match_file = open("output/match.csv", "w")
tournament_file = open("output/tournament.csv", "w")
player_file = open("output/player.csv", "w")



for row in reader:
    line_match = {}
    line_tournament = {}
    line_winner_player = {}
    line_loser_player = {}
    for attr, val in row.items():
        if attr in headers["match"]:
            line_match[attr] = val
            #line_match.append(val)
        if attr in headers["tournament"]:
            line_tournament[attr] = val
            #line_tournament.append(val)
        if attr in headers["winner_player"]:
            line_winner_player[attr] = val
            #line_winner_player.append(val)
        if attr in headers["loser_player"]:
            line_loser_player[attr] = val
            #line_loser_player.append(val)
    preprocessing_match(line_match)

    #match_file.write(','.join(line_match) + "\n")
    #tournament_file.write(','.join(line_tournament) + "\n")
    #player_file.write(','.join(line_winner_player) + "\n")
    #player_file.write(','.join(line_loser_player) + "\n")


tournament_file.close()
player_file.close()
match_file.close()
tennis_file.close()



