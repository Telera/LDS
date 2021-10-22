import pandas as pd
import csv

df_countries = pd.read_csv ('data2021/countries.csv')
#print(df_countries.info())

df_female = pd.read_csv ('data2021/female_players.csv')
#print(df_female.info())

df_male = pd.read_csv ('data2021/male_players.csv')
#print(df_male.info())

df_tennis = pd.read_csv ('data2021/tennis.csv')
for name in zip(df_tennis["winner_name"], df_tennis["loser_name"]):
    print(name)