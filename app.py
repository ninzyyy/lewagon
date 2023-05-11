import streamlit as st
import requests
from datetime import datetime
import pandas as pd

# Remember that there are several ways to output content into your web page...
# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions

st.title('Taxifare')

## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count

col1, col2 = st.columns([1,1])
with col1:
    date = st.date_input(label='Date')
    st.header('Pickup')
    pickup_latitude = st.number_input(label='Pickup Latitude', format='%.7f', value=0.000000, min_value=-90.00000, max_value=90.00000)
    pickup_longitude = st.number_input(label='Pickup Longitude', format='%.7f',value=0.000000, min_value=-180.00000, max_value=180.00000)


with col2:
    time = st.time_input(label='Time')
    st.header('Dropoff')
    dropoff_latitude = st.number_input(label='Dropoff Latitude', format='%.7f', value=0.000000, min_value=-90.00000, max_value=90.00000)
    dropoff_longitude = st.number_input(label='Dropoff Longitude', format='%.7f', value=0.000000, min_value=-180.00000, max_value=180.00000)


passenger_count = st.number_input(label='Passenger Count', min_value=1, max_value=10, step=1)

# Once we have these, let's call our API in order to retrieve a prediction
# See? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
# 🤔 How could we call our API ? Off course... The `requests` package 💡

url = 'https://taxifare.lewagon.ai/predict'

if st.button(label='Submit'):

#if url == 'https://taxifare.lewagon.ai/predict':
    # Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...

# 2. Let's build a dictionary containing the parameters for our API...
    datetime = f'{date} {time}'
    params = {
        "pickup_datetime": datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
        }

# 3. Let's call our API using the `requests` package...
    response = requests.get(url, params=params)

# 4. Let's retrieve the prediction from the **JSON** returned by the API...
    prediction = response.json()['fare']
    rounded_prediction = round(prediction, 2)

# Finally, we can display the prediction to the user
    st.write(f"The fare for this ride would be:")
    st.header(f'{rounded_prediction} $')

# Added a map showing the pickup and dropoff locations.
    map_data = pd.DataFrame()
    map_data['lat'] = [pickup_latitude, dropoff_latitude]
    map_data['lon'] = [pickup_longitude, dropoff_longitude]
    st.map(map_data)
