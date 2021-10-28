def split_date(path):
    with open(path, "r") as f:
        header = f.readline()
        tokens_header = header.strip().split(',')
        for ind, token in enumerate(tokens_header):
            if token == "tourney_date":
                ind_date = ind
        first = True
        file_data = open("output/date.csv", mode='w')
        file_data.write("date_id", "year", "month", "day", "quarter")
        for line in f:
            if first:
                first = False
            else:
                tokens = line.strip().split(',')
                print(tokens)

split_date("data2021/tennis.csv")




