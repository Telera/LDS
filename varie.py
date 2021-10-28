def split_date(path):
    with open(path, "r") as f:
        header = f.readline()
        tokens_header = header.strip().split(',')
        for ind, token in enumerate(tokens_header):
            if token == "tourney_date":
                ind_date = ind
        first = True
        file_data = open("output/date.csv", mode='w')
        file_data.write("date_id,year,month,day,quarter")
        for line in f:
            quarter = 0
            if first:
                first = False
            else:
                tokens = line.strip().split(',')
                year = tokens[ind_date][:4]
                month = int(tokens[ind_date][4:6])
                day = tokens[ind_date][6:8]
                if month <= 3:
                    quarter = "1"
                elif month <= 6:
                    quarter = "2"
                elif month <= 9:
                    quarter = "3"
                else:
                    quarter = "4"
                print(tokens[ind_date],day, month, year,quarter )

split_date("data2021/tennis.csv")




