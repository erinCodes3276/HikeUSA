import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pytz as tz
import matplotlib.pyplot as plt

from datetime import datetime
from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_score

camp_df = pd.read_csv('static/clean_camps.csv')
trails_df = pd.read_csv('static/clean_trails.csv')

hike_usa = pd.DataFrame.merge(camp_df, trails_df,on="code" )
kmeans = KMeans(n_clusters=8, init='k-means++')

# Compute the clusters based on longitude and latitude features
X_sample = hike_usa[['longitude','latitude']].sample(frac=0.1)
kmeans.fit(X_sample)
y = kmeans.labels_
print("k = 8", " silhouette_score ", silhouette_score(X_sample, y, metric='euclidean'))

hike_usa['cluster'] = kmeans.predict(hike_usa[['longitude','latitude']])
print(hike_usa.sample(10))

gdf = hike_usa.groupby(['cluster', 'code']).size().reset_index()
gdf.columns = ['cluster', 'code', 'count']
idx = gdf.groupby(['cluster'])['count'].transform(max) == gdf['count']
tophikes_df = gdf[idx].merge(trails_df, on='code', how='left').sort_values(by='count', ascending=False)

tophikes = tophikes_df[:10]
print(tophikes)
def recommend_venues(df, longitude, latitude):
    predicted_cluster = kmeans.predict(np.array([longitude,latitude]).reshape(1,-1))[0]
    # Fetch the venue name of the top most record in the topvenues dataframe for the predicted cluster
    trail_name = df[df['cluster']==predicted_cluster].iloc[0]['name']
    msg = 'What about visiting the ' + trail_name + '?'
    return msg

print(recommend_venues(tophikes_df, -74, 40.55))
print(recommend_venues(tophikes_df, -73.993, 40.75))