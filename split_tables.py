import csv

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


#print(add_language("data2021/country_list.csv"))
#print(geography_to_csv("data2021/countries.csv"))

tennis_file = open("data2021/tennis.csv", "r")
reader = csv.DictReader(tennis_file)
header = reader.fieldnames

print(header)


headers = {}
headers["match"] = [header[0]] + [header[7]] + [header[14]] + header[21:47]
headers["tournament"] = header[0:5] + header[47:49]

headers["date"] = [header[5]]
headers["player"] = [header[7]] + header[9:13]

print(headers)

#tennis_header_dictionary = dict(zip(range(len(tokens_header)), tokens_header))
#print(tennis_header_dictionary)

match_file = open("output/match.csv", "w")

for row in reader:
    line = []
    for attr, val in row.items():
        if attr in headers["match"]:
            line.append(val)
    match_file.write(','.join(line) + "\n")

"""
for line in tennis_file:
    tokens = line.strip().split(',')



    print(line)

match_header = ""
tournament_header = ""
date_header = ""
player_header = ""
geography = ""


"""
match_file.close()
tennis_file.close()



