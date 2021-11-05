import pandas as pd
import csv

df_date = pd.read_csv ('output/date.csv')

df_geography = pd.read_csv ('output/geography.csv')

df_match = pd.read_csv ('output/match.csv')

df_player = pd.read_csv ('output/player.csv')

df_tournament = pd.read_csv('output/tournament.csv')

match_winner_player = pd.merge(df_player, df_match, left_on='player_id', right_on='winner_id', suffixes=('_w', '_w'))
match_player = pd.merge(df_player, match_winner_player, left_on='player_id', right_on='loser_id', suffixes=('_l','_l'))
print(match_player.info())
