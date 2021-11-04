import csv

def add_language(path):
    country_attribute_ind = 4
    language_attribute_ind = 15
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
        languages[line[country_attribute_ind]] = line[language_attribute_ind][:2]

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
    geography_dict = {}
    corrections = {'Great Britain' : 'United Kingdom',
                   'United States of America' : 'United States',
                   'New Zeland' : 'New Zealand',
                   'Urugay' : 'Uruguay',
                   'North Macedonia' : 'Macedonia',
                   'Unknown' : 'Malaysia'
                   }
    for row in countries_reader:
        geography_dict["country_ioc"] = row["country_code"]

        if row["continent"] == "Unknown":
            geography_dict["continent"] = "Oceania"
        else:
            geography_dict["continent"] = row["continent"]

        if row["country_name"] in corrections.keys():
            geography_dict["language"] = dict_language[corrections[row["country_name"]]]
        else:
            geography_dict["language"] = dict_language[row["country_name"]]
        geography_writer.writerow(geography_dict)
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
