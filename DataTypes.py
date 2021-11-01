import pandas as pd
import csv

df_countries = pd.read_csv ('data2021/countries.csv')
#print(df_countries.info())

df_female = pd.read_csv ('data2021/female_players.csv')
#print(df_female.info())

df_male = pd.read_csv ('data2021/male_players.csv')
#print(df_male.info())

df_tennis = pd.read_csv ('data2021/tennis.csv', low_memory=False)

list = df_tennis["tourney_id"].unique()
for elem in list:
    print(elem)