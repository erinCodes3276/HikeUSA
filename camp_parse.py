import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

import json

def clean_camp():
    state_trails = pd.read_csv('static/ny_campsites.csv')
    camps_df = pd.DataFrame(state_trails)
    drop_col = ['Unnamed: 0', 'cluster']
    camps_df = camps_df.drop(columns=drop_col)
    camps_df.to_csv('clean_camps.csv')
    state_trails = pd.read_csv('static/clean_camps.csv')


def add_point():
    # Create an empty list to store the Point geometries
    geometries = []
    # Iterate through the DataFrame rows
    for index, row in camps_df.iterrows():
        longitude = row['longitude']
        latitude = row['latitude']

        # Create a Point geometry for each row
        point = Point(longitude, latitude)

        # Append the Point geometry to the list
        geometries.append(point)
    return geometries
#geometries = add_point()
# Add the list of Point geometries as a new column 'geometry' in the DataFrame
#camps_df['geometry'] = geometries
state_trails = pd.read_csv('static/clean_camps.csv')
camps_df = pd.DataFrame(state_trails)

camps_df.to_csv('static/clean_camps.csv')
#clean_camp()