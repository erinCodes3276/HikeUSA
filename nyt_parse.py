import geopandas
import pandas as pd
import geopandas as gpd
from flask import Flask, render_template, jsonify
import re


def clean_trails():
    state_trails = pd.read_csv('state-park-trails-1.csv')
    trails_df = pd.DataFrame(state_trails)
    drop_col = ['Fac_unq', 'Alt_Name', 'Asset', 'Asset_unq', 'ATV', 'Colldate', 'Blaze', 'Blaze_2', 'Corridor_W',
                'Tread_Widt', 'Height', 'MotorV', 'Admin', 'Source', 'Abbrev']
    trails_df = trails_df.drop(columns=drop_col)
    trails_df = trails_df.dropna(subset=['Accessible'])
    trails_df = trails_df.dropna(subset=['Foot'])
    trails_df = trails_df.drop(trails_df[trails_df['Foot'] == '-99'].index)
    trails_df = trails_df.drop(trails_df[trails_df['Foot'] == 'I'].index)
    trails_df = trails_df.drop(trails_df[trails_df['Foot'] == 'U'].index)
    trails_df = trails_df.drop(trails_df[trails_df['Accessible'] == 'N'].index)
    trails_df = trails_df.drop(trails_df[trails_df['Condition'] == 'UNDER CONSTRUCTION'].index)
    trails_df = trails_df.dropna(subset=['Condition'])
    trails_df['Accessible'] = trails_df['Accessible'].str.upper()
    trails_df['Condition'] = trails_df['Condition'].str.upper()
    trails_df['Bike'] = trails_df['Bike'].str.upper()
    trails_df.rename(columns={'Name': 'name'}, inplace=True)
    trails_df.rename(columns={'Shape_Leng': 'length'}, inplace=True)
    trails_df.rename(columns={'pref_cs': 'code'}, inplace=True)
    print(trails_df)
    trails_df.to_csv('clean_trails.csv')


trails = pd.read_csv('clean_trails.csv')
trails_df = pd.DataFrame(trails)

trails_df.to_csv('clean_trails.csv', index=False)
# clean_trails()
