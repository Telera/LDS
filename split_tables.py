import csv
import re
import datetime
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

def preprocessing_match(dict, file):
    #tourney_id + match_num
    dict["match_id"] = dict["match_num"]
    del dict["match_num"]

    dict["tourney_id"] = dict["tourney_id"] + "-" + dict["match_id"]
    #file.write(','.join(dict.values()) + "\n")
    file.writerow(dict)

def preprocessing_tournament(dict, file):
    file.writerow(dict)

def preprocessing_player(dict_winner, dict_loser, file):
    dict_winner["player_id"] = dict_winner.pop("winner_id")
    dict_winner["country_id"] = dict_winner.pop("winner_ioc")
    dict_winner["name"] = dict_winner.pop("winner_name")
    dict_winner["hand"] = dict_winner.pop("winner_hand")
    dict_winner["ht"] = dict_winner.pop("winner_ht")

    dict_loser["player_id"] = dict_loser.pop("loser_id")
    dict_loser["country_id"] = dict_loser.pop("loser_ioc")
    dict_loser["name"] = dict_loser.pop("loser_name")
    dict_loser["hand"] = dict_loser.pop("loser_hand")
    dict_loser["ht"] = dict_loser.pop("loser_ht")

    file.writerow(dict_winner)
    file.writerow(dict_loser)

def reformat_date(date):
    return(datetime.datetime.strptime(date, '%Y%m%d').date())

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
match_header = [str.replace('match_num','match_id') for str in headers["match"]]
match_writer = csv.DictWriter(match_file, fieldnames=match_header, lineterminator = '\n')
match_writer.writeheader()

tournament_file = open("output/tournament.csv", "w")
tournament_header = headers["tournament"]
print(tournament_header)
tournament_writer = csv.DictWriter(tournament_file, fieldnames=tournament_header, lineterminator = '\n')
tournament_writer.writeheader()

player_file = open("output/player.csv", "w")
player_header = [str.replace("winner_id" , "player_id").replace("winner_name" , "name").replace("winner_hand" , "hand").replace("winner_ht" , "ht").replace("winner_ioc", "country_id") for str in headers["winner_player"]]
player_header.insert(1, player_header.pop(-1))
player_writer = csv.DictWriter(player_file, fieldnames=player_header, lineterminator = '\n')
player_writer.writeheader()



for row in reader:
    line_match = {}
    line_tournament = {}
    line_winner_player = {}
    line_loser_player = {}
    for attr, val in row.items():
        if attr in headers["match"]:
            line_match[attr] = val
        if attr in headers["tournament"]:
            line_tournament[attr] = val
        if attr in headers["winner_player"]:
            line_winner_player[attr] = val
        if attr in headers["loser_player"]:
            line_loser_player[attr] = val
    preprocessing_match(line_match, match_writer)
    preprocessing_tournament(line_tournament, tournament_writer)
    preprocessing_player(line_winner_player, line_loser_player, player_writer)



tournament_file.close()
player_file.close()
match_file.close()
tennis_file.close()



