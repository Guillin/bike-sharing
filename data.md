# EcoBici (bike sharing trips)

EcoBici Bike sharing data includes all trips made with city bikes sharing of Buenos Aires City. The dataset includes information about trip’s origin and destination stations, origin and destination geocords, start and end times, duration (in minutes) and gender.

The data is available from 2019 to 2023. It will be updated montly.


## Files

- *bike_share_baires.parquet* : parquet file partitioned by year whit bicicly trips information.
- *baires-neighborhoods.geojson*:  Buenos Aires neighborhoods polygons and correlated data with their respective names.

## Columns

- *rout_id*: the ID of the bike trip.
- *duration*: Amount of time ride takes in (min). How much time has passed between the start and the end of the ride.
- *departure*: Departure date time.
- *departure_station_id*: The ID of departure bike station.              
- *departure_station_name*: The name of departure bike station.            
- *departure_address*: The address of departure bike station.                  
- *departure_long*: The longitude coordinate of the departure bike station.                   
- *departure_lat*: The latitude coordinate of the departure bike station.                    
- *return*: Return date time.                   
- *return_station_id*: The ID of return bike station.            
- *return_station_name*: The name of destination bike station.                
- *return_station_address*: The address of return bike station.          
- *return_station_long*: The longitude coordinate of the return bike station.             
- *return_station_lat*: The latitude coordinate of the return bike station.             
- *user_id*: User's Id who take the bike trip.                           
- *bicycle_type*: the name of the bicycle type                      
- *gender*: User's gender who take the bike trip                             
- *year*: Year in which the trip was made.