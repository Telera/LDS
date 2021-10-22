



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
                print(ind, token, line)
                if token == '':
                    missing_count[ind] += 1
        print(missing_count)
        return(count, max_col, min_col)


print(min_max_columns("data2021/female_players.csv"))
