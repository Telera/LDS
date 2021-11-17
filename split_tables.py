import csv
import re
import datetime
from pathlib import Path

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

def reformat_date(date):
    return(datetime.datetime.strptime(date, '%Y%m%d').date())

def preprocessing_match(dict, file, id):
    #match_num + tourney_id
    dict["match_id"] = dict.pop("match_num")

    dict["match_id"] =str(id) + "-" + dict["match_id"] + "-" + dict["tourney_id"]

    file.writerow(dict)

def preprocessing_tournament(dict, file):
    dict["date_id"] = dict.pop("tourney_date")
    file.writerow(dict)

def year_of_birth(date, age):
    date = reformat_date(date)
    year = date.year
    fist_gen = str(date.year) + "01" + "01"
    first_gen_next_year = str(date.year + 1) + "01" + "01"
    startOfThisYear = reformat_date(fist_gen)
    startOfNextYear = reformat_date(first_gen_next_year)
    delta = date - startOfThisYear
    yearDuration = startOfNextYear - startOfThisYear
    fraction = delta/yearDuration
    date_fraction = (date.year) + fraction
    birth = date_fraction - float(age)
    return(int(birth))

def preprocessing_player(dict, file, year_of_birth, sex):
    dict_player = {}
    for key,val in dict.items():
        if key == "winner_id" or key == "loser_id":
            dict_player["player_id"] = dict[key]
        if key == "winner_name" or key == "loser_name":
            dict_player["name"] = dict[key]
        if key == "winner_hand" or key == "loser_hand":
            dict_player["hand"] = dict[key]
        if key == "winner_ht" or key == "loser_ht":
            dict_player["ht"] = dict[key]
        if key == "winner_ioc" or key == "loser_ioc":
            dict_player["country_id"] = dict[key]

    dict_player["year_of_birth"] = year_of_birth
    dict_player["sex"] = sex
    file.writerow(dict_player)

def create_gender_sets():
    male_file = open("data2021/male_players.csv", "r")
    reader_male = csv.DictReader(male_file)
    female_file = open("data2021/female_players.csv", "r")
    reader_female = csv.DictReader(female_file)
    players = (reader_male, reader_female)
    dict_set = {"male": set(), "female": set()}
    for player_gender in players:
        for row in player_gender:
            if player_gender == reader_male:
                dict_set["male"].add(row["name"].replace("Mr ", "").replace("Mr", "").lower() + " " + row["surname"].lower())
            else:
                dict_set["female"].add(row["name"].replace("Mrs ", "").replace("Mrs", "").lower() + " " + row["surname"].lower())
    male_file.close()
    female_file.close()
    return(dict_set)

def preprocessing_date(file, date):
    tourney_date = reformat_date(date)
    dict = {}
    dict["date_id"] = date
    dict["day"] = tourney_date.day
    dict["month"] = tourney_date.month
    dict["year"] = tourney_date.year
    dict["quarter"] = (tourney_date.month - 1) // 3 + 1
    file.writerow(dict)

tennis_file = open("data2021/tennis.csv", "r")
reader = csv.DictReader(tennis_file)
header = reader.fieldnames
print(header)


headers = {}
headers["match"] = [header[0]] + header[6:8] + [header[14]] + header[21:47]
headers["tournament"] = header[0:6] + header[47:49]
headers["winner_player"] = [header[7]] + header[9:13]
headers["loser_player"] = [header[14]] + header[16:20]
headers["date"] = [header[5]]
print(headers)

match_file = open("output/match.csv", "w")
match_header = [str.replace('match_num','match_id') for str in headers["match"]]
match_writer = csv.DictWriter(match_file, fieldnames=match_header, lineterminator = '\n')
match_writer.writeheader()

tournament_file = open("output/tournament.csv", "w")
tournament_header = headers["tournament"]
tournament_header = [str.replace('tourney_date','date_id') for str in headers["tournament"]]
tournament_header.insert(1, tournament_header.pop(5))
tournament_writer = csv.DictWriter(tournament_file, fieldnames=tournament_header, lineterminator = '\n')
tournament_writer.writeheader()

player_file = open("output/player.csv", "w")
player_header = [str.replace("winner_id" , "player_id").replace("winner_name" , "name").replace("winner_hand" , "hand").replace("winner_ht" , "ht").replace("winner_ioc", "country_id") for str in headers["winner_player"]]
player_header.insert(1, player_header.pop(-1))
player_header.insert(3, "sex")
player_header.append("year_of_birth")
player_writer = csv.DictWriter(player_file, fieldnames=player_header, lineterminator = '\n')
player_writer.writeheader()

date_file = open("output/date.csv", "w")
date_header = ["date_id", "day", "month","year" , "quarter"]
date_writer = csv.DictWriter(date_file, fieldnames=date_header, lineterminator = '\n')
date_writer.writeheader()

set_id_tournament = set()
set_id_player = set()
set_id_date = set()

sets_player_gender = create_gender_sets()

match_id_count = 0
for row in reader:
    line_match = {}
    line_tournament = {}
    line_winner_player = {}
    line_loser_player = {}
    curr_date = {}

    for attr, val in row.items():
        if attr == "tourney_date":
            curr_date[attr] = val
        if attr in headers["match"]:
            line_match[attr] = val
        if attr in headers["tournament"]:
            line_tournament[attr] = val
        if attr in headers["winner_player"]:
            line_winner_player[attr] = val
        if attr in headers["loser_player"]:
            line_loser_player[attr] = val


    preprocessing_match(line_match, match_writer, match_id_count)
    match_id_count += 1

    if line_tournament["tourney_id"] not in set_id_tournament:
        set_id_tournament.add(line_tournament["tourney_id"])
        preprocessing_tournament(line_tournament, tournament_writer)


    if line_winner_player["winner_id"] not in set_id_player:
        set_id_player.add(line_winner_player["winner_id"])
        if row["winner_age"] != "":
            winner_year_of_birth = year_of_birth(row["tourney_date"], row["winner_age"])
        winner_name = row["winner_name"].replace("-", " ").replace("'", "").lower()
        if winner_name in sets_player_gender["male"]:
            sex_winner_player = "M"
        elif winner_name in sets_player_gender["female"]:
            sex_winner_player = "F"
        else:
            sex_winner_player = ""
        preprocessing_player(line_winner_player, player_writer, winner_year_of_birth, sex_winner_player)

    loser_year_of_birth = ""
    winner_year_of_birth = ""

    if line_loser_player["loser_id"] not in set_id_player:
        set_id_player.add(line_loser_player["loser_id"])
        if row["loser_age"] != "":
            loser_year_of_birth = year_of_birth(row["tourney_date"], row["loser_age"])
        loser_name = row["loser_name"].replace("-", " ").replace("'", "").lower()
        if loser_name in sets_player_gender["male"]:
            sex_loser_player = "M"
        elif loser_name in sets_player_gender["female"]:
            sex_loser_player = "F"
        else:
            sex_loser_player = ""
        preprocessing_player(line_loser_player, player_writer, loser_year_of_birth, sex_loser_player)

    if curr_date["tourney_date"] not in set_id_date:
        set_id_date.add(curr_date["tourney_date"])
        preprocessing_date(date_writer, row["tourney_date"])

tournament_file.close()
player_file.close()
match_file.close()
tennis_file.close()



create_gender_sets()