#pip install gender_guesser
import gender_guesser.detector as gender
import pandas as pd
import re

"""
def fill_missing_sex(path):
    df_player = pd.read_csv(path)
    df_missing_sex = df_player[df_player["sex"].isnull()]
    missing_sex_patter = list(map(lambda x: re.search('[A-Z][a-z]+', x), df_missing_sex["name"]))
    missing_sex_name = list(map(lambda x: x.group(0), missing_sex_patter))
    print(missing_sex_name)
    detector = gender.Detector()
    print(list(map(lambda x: detector.get_gender(x), missing_sex_name)))
"""

def fill_missing_sex(path_player, path_match):
    players = pd.read_csv(path_player)
    match = pd.read_csv(path_match)
    players_selection = match[['winner_id', 'loser_id']]
    sex = players[['player_id', 'sex']]
    winner_sex = pd.merge(players_selection, sex, left_on="winner_id", right_on="player_id").drop('winner_id', axis=1)
    players_sex = pd.merge(winner_sex, sex, left_on="loser_id", right_on="player_id").drop('loser_id', axis=1)
    players_sex.rename(columns={'player_id_x': 'winner', 'sex_x': 'winner_sex', 'player_id_y': 'loser', 'sex_y': 'loser_sex'},inplace=True)

    winner_id = players_sex[players_sex["winner_sex"].isnull()]["winner"].unique()
    loser_id = players_sex[players_sex["loser_sex"].isnull()]["loser"].unique()

    #print(set(winner_id) == set(loser_id))
    #both sets are equal

    print(winner_id)
    players_with_sex_missing = players_sex[players_sex['winner'].isin(winner_id)].sort_values(by="winner")
    #set(players_with_sex_missing.groupby(["winner", "loser_sex"])["loser_sex"].agg("size")) == set(players_with_sex_missing.groupby(["winner", "loser_sex"]).agg("size").sort_index())
    #all players have played with people with same sex for this reason we can remove duplicates
    missing_sex_values = players_sex[players_sex['winner'].isin(winner_id)].drop_duplicates(subset="winner")

    missing_sex_values.drop(columns=["winner_sex", "loser"], axis=1, inplace=True)
    missing_sex_values.rename(columns={'winner': 'player', 'loser_sex': 'sex'}, inplace=True)
    print(missing_sex_values)

    players_full = players.set_index("player_id").combine_first(missing_sex_values.set_index("player")).reset_index()
    players_full.rename(columns={'index': 'player_id'}, inplace=True)
    cols_order = ['player_id', 'country_id', 'name', 'sex', 'hand', 'ht', 'year_of_birth']
    players_full = players_full[cols_order]
    return(players_full)


    #print(players['sex'].isnull().sum())
    #print(players.info())

fill_missing_sex("output/player.csv", "output/match.csv")
