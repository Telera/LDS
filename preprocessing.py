
import csv

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
                    if len_str[ind] < len(token):
                        len_str[ind] = len(token)
        return(len_str)

print(count_max_len_str("data2021/countries.csv"))