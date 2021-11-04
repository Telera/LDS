from bs4 import BeautifulSoup
import requests


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

    url = 'https://www.loc.gov/standards/iso639-2/php/code_list.php'
    dashboardFile = requests.get(url, allow_redirects=True)
    open('', 'wb').write(dashboardFile.content)

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

print(add_language("data2021/country_list.csv"))
print(geography_to_csv("data2021/countries.csv"))