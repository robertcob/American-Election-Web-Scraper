import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
from shapely.geometry import Point, Polygon
import numpy as np



poly_States = gpd.read_file("electoral_Map_Final.shp")

null_Color = "#29ff4d"
tie_Color = "#806d4b"

tilt_R = "#ffc0cb"
lean_R ="#FF0000"
safe_R = "#8B0000"

tilt_B = "#87CEFA"
lean_B ="#00BFFF"
safe_B = "#0000FF"
def state_Plotter():

    fig, ax = plt.subplots(figsize=(30, 30))
    gf = gpd.read_file("electoral_Map_Final.dbf")

    for trump, biden, state in zip(gf.TrumpAVG, gf.BidenAVG, gf.STATE_NAME):
        if state == "California":
            trump, biden = biden ,trump
        if trump == "null" and biden == "null":
            poly_States[poly_States.STATE_NAME == state].plot(ax=ax, edgecolor='white', linewidth=1.5, color=null_Color)
            continue

        trump = int(trump)
        biden = int(biden)

        if trump == biden:
            poly_States[poly_States.STATE_NAME == state].plot(ax=ax, edgecolor='white', linewidth=1.5, color=tie_Color)
        else:
            if trump - biden > 0:
                if trump - biden < 5:
                    poly_States[poly_States.STATE_NAME == state].plot(ax=ax,edgecolor='white', linewidth=1.5, color = tilt_R)

                elif trump - biden > 5 and trump - biden < 10:
                    poly_States[poly_States.STATE_NAME == state].plot(ax=ax, edgecolor='white', linewidth=1.5, color=lean_R)

                else:
                    poly_States[poly_States.STATE_NAME == state].plot(ax=ax, edgecolor='white', linewidth=1.5, color=safe_R)

            else:
                if biden - trump < 5:
                    poly_States[poly_States.STATE_NAME == state].plot(ax=ax, edgecolor='white', linewidth=1.5,
                                                                      color=tilt_B)
                elif biden - trump > 5 and biden - trump < 10:
                    poly_States[poly_States.STATE_NAME == state].plot(ax=ax, edgecolor='white', linewidth=1.5,
                                                                      color=lean_B)
                else:
                    poly_States[poly_States.STATE_NAME == state].plot(ax=ax, edgecolor='white', linewidth=1.5,
                                                                      color=safe_B)







list_Of_States = states = ["AL", "AK",  "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI",
           "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]




us_map = state_Plotter()

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show()