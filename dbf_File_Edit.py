from database_Read_Operations import *
content = find_Averages()
import geopandas as gpd

#setting up dataframe

gf = gpd.read_file("electoral_Map_Final.dbf")


trumpAvg = []
bidenAvg = []
spread = []
electoral_Vote = []
electoral_Vote_Dict = {
    "Alabama": 9,
    "Alaska": 3,
    "Arizona": 11,
    "Arkansas":6,
    "California": 55,
    "Colorado": 9,
    "Connecticut":7,
    "Delaware":3,
    "District of Columbia": 3,
    "Florida": 29,
    "Georgia": 16,
    "Hawaii": 4,
    "Idaho": 4,
    "Illinois": 20,
    "Indiana": 11,
    "Iowa": 6,
    "Kansas":6,
    "Kentucky": 8,
    "Louisiana": 8,
    "Maine": 4,
    "Maryland": 10,
    "Massachusetts":11,
    "Michigan":16,
    "Minnesota":10,
    "Mississippi": 6,
    "Missouri": 10,
    "Montana":3,
    "Nebraska":5,
    "Nevada":6,
    "New Hampshire": 4,
    "New Jersey": 14,
    "New Mexico":5,
    "New York": 29,
    "North Carolina":15,
    "North Dakota":3,
    "Ohio": 18,
    "Oklahoma":7,
    "Oregon":7,
    "Pennsylvania":20,
    "Rhode Island":4,
    "South Carolina": 9,
    "South Dakota":3,
    "Tennessee":11,
    "Texas":38,
    "Utah":6,
    "Vermont":3,
    "Virginia": 13,
    "Washington":12,
    "West Virginia":5,
    "Wisconsin":10,
    "Wyoming":3
}


for state in gf.STATE_NAME:
    electoral_Vote.append(electoral_Vote_Dict[state])

    try:
        value = content[state]
        trumpAvg.append(value[0])
        bidenAvg.append(value[1])
        spread.append(value[2])

    except KeyError:
        trumpAvg.append("null")
        bidenAvg.append("null")
        spread.append("null")

gf["TrumpAVG"] = trumpAvg
gf["BidenAVG"] = bidenAvg
gf["Spread"] = spread
gf["ElectoralVotes"] = electoral_Vote

gf.to_file("electoral_Map_Final.dbf")

for col in gf.columns:
    print(col)