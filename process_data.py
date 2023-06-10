import pandas as pd
import numpy as np
import os
import gc
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

PATH = "data"
print("\n::INIT::\n")

df_bike_trip = pd.DataFrame()

end_column_names = [ 
                'rout_id', 'duration', 'departure', 'departure_station_id',
                'departure_station_name', 'departure_address',
                'departure_long', 'departure_lat', 'return', 'return_station_id',
                'return_station_name', 'return_station_address', 'return_station_long', 
                'return_station_lat', 'user_id', 'bicycle_type', 'gender'
               ]


year=2019
file_name = f"trips_{year}.csv"
print("Loading dataset ",  file_name, "\n")
df_bike_trip_y2019 = pd.read_csv(os.path.join(PATH, "raw", file_name),  index_col=[0])#.iloc[:, :17]
df_bike_trip_y2019.columns = end_column_names
df_bike_trip_y2019["year"] = year


year=2020
file_name = f"trips_{year}.csv"
print("Loading dataset ",  file_name, "\n")
df_bike_trip_y2020 = pd.read_csv(os.path.join(PATH, "raw", file_name),  index_col=[0])
df_bike_trip_y2020.columns = end_column_names
df_bike_trip_y2020["year"] = year


year=2021
file_name = f"trips_{year}.csv"
print("Loading dataset ",  file_name, "\n")
df_bike_trip_y2021 = pd.read_csv(os.path.join(PATH, "raw", file_name),  index_col=[0])
df_bike_trip_y2021["género"] = np.where(df_bike_trip_y2021["género"].isnull(), df_bike_trip_y2021["Género"], df_bike_trip_y2021["género"] )
df_bike_trip_y2021 = df_bike_trip_y2021.iloc[:, :17]
df_bike_trip_y2021.columns = end_column_names
df_bike_trip_y2021["year"] = year


year=2022
file_name = f"trips_{year}.csv"
print("Loading dataset ",  file_name, "\n")
df_bike_trip_y2022 = pd.read_csv(os.path.join(PATH, "raw", file_name),  index_col=[0]).iloc[:, 1:18]
df_bike_trip_y2022.columns = end_column_names
df_bike_trip_y2022["year"] = year


year=2023
file_name = f"trips_{year}.csv"
print("Loading dataset ",  file_name, "\n")
df_bike_trip_y2023 = pd.read_csv(os.path.join(PATH, "raw", file_name),  index_col=[0])
df_bike_trip_y2023.columns = end_column_names
df_bike_trip_y2023["year"] = year

# Concatenate first 3 dataset because they have same structure
df_bike_trip = pd.concat([df_bike_trip_y2019, df_bike_trip_y2020, df_bike_trip_y2021], ignore_index=True)

del df_bike_trip_y2019, df_bike_trip_y2020, df_bike_trip_y2021
gc.collect()

print("Fixing coord data from 2019 to 2021 dataset. \n")
# This code fix return station long and lat variables on dataset from 2019 to 2021. Lat and Long come together, so they have to be splitted.
return_station_coord = [coord for coord in tqdm(df_bike_trip["return_station_lat"].str.split(","))]

return_station_long_ = []
return_station_lat_ = []
for coord in tqdm(return_station_coord):
    if coord is np.nan:
        return_station_long_.append(np.nan)
        return_station_lat_.append(np.nan)
        
    else:
        return_station_lat_.append(coord[0])
        return_station_long_.append(coord[1])
        
df_bike_trip["return_station_long"] = return_station_long_
df_bike_trip["return_station_lat"] = return_station_lat_
df_bike_trip["return_station_long"] = df_bike_trip["return_station_long"].astype(float)
df_bike_trip["return_station_lat"] = df_bike_trip["return_station_lat"].astype(float)

df_bike_trip = pd.concat([df_bike_trip, df_bike_trip_y2022, df_bike_trip_y2023], ignore_index=True)

del df_bike_trip_y2022, df_bike_trip_y2023
gc.collect()

# Data type conversion
df_bike_trip["return_station_long"] = df_bike_trip["return_station_long"].astype(float)
df_bike_trip["return_station_lat"] = df_bike_trip["return_station_lat"].astype(float)
df_bike_trip["departure"] = pd.to_datetime(df_bike_trip["departure"])
df_bike_trip["return"] = pd.to_datetime(df_bike_trip["return"])

# Re calculate duration in minutes 
df_bike_trip.loc[:, 'duration'] = (df_bike_trip["return"] - df_bike_trip["departure"]) / pd.Timedelta(minutes=1)

# drop rows that has null values. Those who don't have return point
df_bike_trip = df_bike_trip.dropna()

# select and re arrange final dataframe
df_bike_trip = df_bike_trip.loc[:,['rout_id', 'duration', 'departure', 'departure_station_id',
       'departure_station_name', 'departure_address', 'departure_long',
       'departure_lat', 'return', 'return_station_id', 'return_station_name',
       'return_station_address', 'return_station_long', 'return_station_lat',
       'user_id', 'bicycle_type', 'gender', 'year']]

print("Saving final dataset.\n")
# Save final dataset
df_bike_trip.to_parquet(os.path.join(PATH, "bike_share_baires.parquet"), partition_cols=["year"]) 
print("\n::END::\n")
