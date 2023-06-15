import math
import pandas as pd
from shapely.wkt import loads
import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two points on the Earth's surface using the Haversine formula.
    Arguments:
    lat1 -- latitude of point 1
    lon1 -- longitude of point 1
    lat2 -- latitude of point 2
    lon2 -- longitude of point 2
    Returns:
    Distance between the two points in kilometers.
    """
    # Convert latitude and longitude from degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Radius of the Earth in kilometers
    radius = 6371

    # Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(
        dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance


def get_coords(multiline):
    for line_string in multiline:
        for coordinates in line_string.coords:
            lon, lat = coordinates
    return lon, lat


def min_distance(df, lat, lon):
    distances = []
    for index, row2 in df.iterrows():
        lon2 = row2[1]
        lat2 = row2[2]
        distance = haversine_distance(lat, lon, lat2, lon2)
        distances.append(distance)
    min_distance = min(distances)
    distance_index = distances.index(min_distance)
    return min_distance, distance_index


campsite_data = pd.read_csv('static/clean_camps.csv')
camp_df = pd.DataFrame(campsite_data)
trail_data = pd.read_csv('static/clean_trails.csv')
trail_df = pd.DataFrame(trail_data)
pref_cs = []
for index, row in trail_df.iterrows():
    trail_coord = row['the_geom']
    multiline = loads(trail_coord).geoms
    lon, lat = get_coords(multiline)
    distance, distance_index = min_distance(camp_df, lat, lon)
    campsite = camp_df.loc[distance_index, 'name']
    trail_len = row['length']
    cs_code = camp_df.loc[distance_index, 'code']
    pref_cs.append(cs_code)
    print(campsite)
    print("is",distance,"km from trail with length", trail_len)
trail_df['pref_cs'] = pref_cs
print(trail_df['pref_cs'].unique())
trail_df.to_csv('clean_trails.csv')
