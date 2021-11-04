import csv

def add_language(path):
    num_commented_rows = 50
    file_language = open(path, "r")
    r = csv.reader(file_language, delimiter="\t")
    for skip in range(num_commented_rows):
        next(r)
    header = file_language.readline()
    tokens_header = header.strip().split('\t')
    print(tokens_header)
    languages = {}
    for line in r:
        languages[line[1]] = line[15][:2]

    file_language.close()
    return(languages)

def geography_to_csv(path):
    dict_language = add_language("languages.txt")
    file_continent = open(path, "r")
    countries_reader = csv.DictReader(file_continent)
    header = countries_reader.fieldnames

    geography_file = open("output/geography.csv", "w")
    geography_header = ["country_ioc", "continent", "language"]
    geography_writer = csv.DictWriter(geography_file, fieldnames=geography_header, lineterminator='\n')
    geography_writer.writeheader()


    for row in countries_reader:
        dict_language[row["country_code"]]




    for ind, token in enumerate(tokens_header):
        if token == "country_code":
            ind_code = ind
        if token == "continent":
            ind_continent = ind
    first = True
    file_continent = open("geography.csv", mode='a')
    file_continent.write("country_ioc,continent,language")
    for line in f:
        if first:
            first = False
        else:
            tokens = line.strip().split(',')
            diz_language = add_language("data2021/country_list.csv")
            row = []
            row.append(tokens[ind_code])
            row.append(tokens[ind_continent])
            row.append(dict_language[tokens[ind_country]])
            print(row)
            #todo write row in the file

    file_continent.close()

import urllib.request
import os

def download_file(url,local_file, force=False):
    if not os.path.exists(local_file) or force:
        print('Downloading',url,'to',local_file)
        with urllib.request.urlopen(url) as opener, \
             open(local_file, mode='w', encoding='utf-8') as outfile:
                    outfile.write(opener.read().decode('utf-8'))
    else:
        print(local_file,'already downloaded')


#download_file("http://download.geonames.org/export/dump/countryInfo.txt", "languages.txt")
geography_to_csv("data2021/countries.csv")
