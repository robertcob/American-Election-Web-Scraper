import pymongo

global mydb
global mycol


# def database_Creation():
#     try:
#         db_Name = "Polling_Data"
#         col_Name = "Trump_Vs_Biden_V1"
#         myClient = pymongo.MongoClient("mongodb://localhost:27017/")
#         global mydb
#         global mycol
#
#         mydb = myClient[db_Name]
#         mycol = mydb[col_Name]
#         # print("Now using database", mydb, "And collection", mycol, "\n")
#     except IndexError as err:
#         print("IndexError - Script needs more arguments for MongoDB db and col name:", err)
#         quit()

# safe_Blue = ["California", "Oregan", "Washington", "Neveda", "Colorado", "New Mexico", "Minnesota", "Illinois", "Maryland", "Delaware", "Connecticut", "Rhode Island", "Connecticut", "Vermont" , "Maine"]
# try:
#     db_Name = "Polling_Data"
#     col_Name = "Trump_Vs_Biden_V1"
#     myClient = pymongo.MongoClient("mongodb://localhost:27017/")
#
#
#     mydb = myClient[db_Name]
#     mycol = mydb[col_Name]
#     # print("Now using database", mydb, "And collection", mycol, "\n")
# except IndexError as err:
#     print("IndexError - Script needs more arguments for MongoDB db and col name:", err)
#     quit()
#
# for poll in mycol.find():
#     for state in safe_Blue:
#         if poll["State"] == state:
#             poll["Trump"], poll["Biden"] = poll["Biden"], poll["Trump"]
#
# import dbf
# from dbfread import DBF
# from pandas import DataFrame
# import geopandas as gpd
# import numpy as np
# table = DBF("C:/Users/rober/Downloads/cb_2016_us_state_500k/cb_2016_us_state_500k.dbf")
# frame = DataFrame(iter(table))
# # table = dbf.Table("C:/Users/rober/Downloads/cb_2016_us_state_500k/cb_2016_us_state_500k.dbf")
# gf = gpd.read_file("C:/Users/rober/Downloads/cb_2016_us_state_500k/cb_2016_us_state_500k.dbf")
# gf.to_file("export.dbf")


import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.geometry import Point, Polygon
import numpy as np

# poly_States = gpd.read_file("states_Final.shp")
poly_States = gpd.read_file("electoral_Map_Final.shp")
gf = gpd.read_file("electoral_Map_Final.dbf")

for trump, biden in zip(gf.TrumpAVG, gf.BidenAVG):

    if trump == "null" and biden == "null":
        continue
    else:
        if trump - biden >0:
            if trump - biden < 5:
                #display state as lean red
            elif trump - biden > 5 and trump-biden < 10:
                #display state as likely red
            else:
                #safe red
        else:
            if biden - trump < 5:
                #display as lean blue
            elif biden - trump > 5 and biden-trump < 10:
                # display state as likely blue
            else:
                #safe red



# hawaii = poly_States[poly_States.STATE_ABBR == "HI"]
# coords = [i for i in hawaii.geometry]
#
# all_Coords = []
# for b in coords[0].boundary:
#     coords = np.dstack(b.coords.xy).tolist()
#     all_Coords.append(*coords)
#
# for cord_1 in all_Coords:
#     for cord2 in cord_1:
#         cord2[0] = cord2[0] + 54.00000000000000



# poly_States.plot()
# plt.show()