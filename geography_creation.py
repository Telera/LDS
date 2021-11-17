import csv
import urllib.request
import os
from pathlib import Path


#function used to download our file with all languages
def download_file(url,local_file, force=False):
    if not os.path.exists(local_file) or force:
        print('Downloading',url,'to',local_file)
        with urllib.request.urlopen(url) as opener, \
             open(local_file, mode='w', encoding='utf-8') as outfile:
                    outfile.write(opener.read().decode('utf-8'))
    else:
        print(local_file,'already downloaded')


def add_language(path):
    # check if language.txt is already been downloaded
    if not language_file.is_file():
        download_file("http://download.geonames.org/export/dump/countryInfo.txt", path)
        print("File downloaded from http://download.geonames.org/export/dump/countryInfo.txt")

    country_attribute_ind = 4
    language_attribute_ind = 15
    num_commented_rows = 50 #the first 50 rows are not useful for the analysis so we skip them
    file_language = open(path, "r")
    r = csv.reader(file_language, delimiter="\t")
    for skip in range(num_commented_rows):
        next(r)
    header = file_language.readline()
    tokens_header = header.strip().split('\t')
    languages = {}
    for line in r:
        #[:2] is specified in order to pick only the first language of those spoken in that country
        #(language is a code composed by 2 letters)
        languages[line[country_attribute_ind]] = line[language_attribute_ind][:2]

    file_language.close()
    return(languages)

def geography_to_csv(path, language_file):
    dict_language = add_language(language_file)
    file_continent = open(path, "r")
    countries_reader = csv.DictReader(file_continent)
    header = countries_reader.fieldnames
    geography_output = Path("output/geography.csv")
    geography_file = open(geography_output, "w")
    geography_header = ["country_ioc", "continent", "language"]
    geography_writer = csv.DictWriter(geography_file, fieldnames=geography_header, lineterminator='\n')
    geography_writer.writeheader()
    geography_dict = {}
    corrections = {'Great Britain' : 'United Kingdom',
                   'United States of America' : 'United States',
                   'New Zeland' : 'New Zealand',
                   'Urugay' : 'Uruguay',
                   'North Macedonia' : 'Macedonia',
                   'Unknown' : 'Malaysia' #The IOC code is POC that corresponds to Pacific Oceania, not present in language.txt file so we have substituted it with Malaysia because the language is the same
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

language_file = Path("languages.txt")
geography_to_csv("data2021/countries.csv", language_file)
