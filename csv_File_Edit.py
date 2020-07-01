import csv
from database_Read_Operations import *
import pandas as pd
map_Info = find_Averages()


with open("us_States.csv", "r") as state_Csv:
    df = pd.read_csv("us_States.csv", delimiter=',')
    column_Headers = []
    for header in df.columns:
        column_Headers.append(header)

    abbrevs = [column_Headers[0]]
    lats = [column_Headers[1]]
    longs = [column_Headers[2]]
    states = [column_Headers[3]]

    for (abbrev, lat, long, state) in zip(df.Abbrev, df.Latitude, df.Longitude, df.State):
        abbrevs.append(abbrev)
        lats.append(lat)
        longs.append(long)
        states.append(state)

    trumpAvg = ["TrumpAvg"]
    bidenAvg = ["BidenAvg"]
    spread = ["Spread"]

    for state in states:
        if state in column_Headers:
            continue
        try:
            value = map_Info[state]
            trumpAvg.append(value[0])
            bidenAvg.append(value[1])
            spread.append(value[2])

        except KeyError:
            trumpAvg.append("NULL")
            bidenAvg.append("NULL")
            spread.append("NULL")

    wtr = csv.writer(open("out.csv", "w"), delimiter=',', lineterminator='\n')
    for abbrev, lat, long, state, trump, biden, spread in zip(abbrevs,lats, longs, states, trumpAvg, bidenAvg, spread):
        arr = [abbrev, lat, long, state, trump, biden, spread]
        wtr.writerow(arr)



# for state, avg1, avg2, spread in zip(states,trumpAvg,bidenAvg,spread):
#     print("|||" ,state, avg1, avg2, spread, "|||")






