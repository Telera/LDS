
import csv

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def min_max_columns(path):
    with open(path,'r') as f:
        count = 0
        max_col = float('-inf')
        min_col = float('inf')
        header = f.readline()
        tokens_header = header.strip().split(',')
        missing_count = [0] * len(tokens_header)
        for line in f:
            count +=1
            tokens = line.strip().split(',')
            max_col = max(max_col, len(tokens))
            min_col = min(min_col, len(tokens))
            for ind, token in enumerate(tokens):
                if token == '':
                    missing_count[ind] += 1
        return(count, max_col, min_col, missing_count)



def count_max_len_str(path):
    with open(path,'r') as f:
        first = True
        header = f.readline()
        tokens_header = header.strip().split(',')
        len_str = [0] * len(tokens_header)
        for line in f:
            if first:
                first = False
            else:
                tokens = line.strip().split(',')
                for ind, token in enumerate(tokens):
                    if is_number(token):
                        len_str[ind] = "int"
                    else:
                        if len_str[ind] < len(token):
                            len_str[ind] = len(token)
        return(len_str)



print(min_max_columns("data2021/countries.csv"))
print(min_max_columns("data2021/female_players.csv"))
print(min_max_columns("data2021/male_players.csv"))
print(min_max_columns("data2021/tennis.csv"))

print(count_max_len_str("data2021/countries.csv"))
print(count_max_len_str("data2021/female_players.csv"))
print(count_max_len_str("data2021/male_players.csv"))
print(count_max_len_str("data2021/tennis.csv"))