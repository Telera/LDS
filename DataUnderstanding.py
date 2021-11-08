import pandas as pd
import csv

df_date = pd.read_csv ('output/date.csv')

df_geography = pd.read_csv ('output/geography.csv')

df_match = pd.read_csv ('output/match.csv')

df_player = pd.read_csv ('output/player.csv')

df_tournament = pd.read_csv('output/tournament.csv')

match_winner_player = pd.merge(df_player, df_match, left_on='player_id', right_on='winner_id')
match_player = pd.merge(df_player, match_winner_player, left_on='player_id', right_on='loser_id')
match_player.rename(columns={'player_id_x': 'winner_id', 'sex_x': 'winner_sex', 'player_id_y': 'loser_id', 'sex_y': 'loser_sex'}, inplace = True)
print(match_player)

sex_control = match_player.dropna()
equal_sex = sex_control["winner_sex"] == sex_control["loser_sex"]
print(equal_sex.value_counts())


