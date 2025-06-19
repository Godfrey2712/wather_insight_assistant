import requests
import pandas as pd
import os

#### This is just to test api endpoint. This is done on MS Fabric ####

# Define API endpoint and parameters
url = "https://meteostat.p.rapidapi.com/point/hourly"
params = {
    "lat": "43.6667",       # Latitude (e.g. Toronto)
    "lon": "-79.4",         # Longitude
    "alt": "113",           # Altitude in meters
    "start": "2020-01-01",  # Start date
    "end": "2020-01-29",    # End date
    "tz": "America/Toronto" # Timezone
}

headers = {
    "x-rapidapi-host": "meteostat.p.rapidapi.com",
    "x-rapidapi-key": os.getenv("X-Rapidapi-Key")
}

# Make the API call
try:
    response = requests.get(url, headers=headers, params=params, timeout=60)
    response.raise_for_status()
    data = response.json().get("data", [])

    if data:
        df = pd.DataFrame(data)
        #df.to_parquet("toronto_weather_2020_01_01.parquet", index=False)
        print("✅ Data saved to toronto_weather_2020_01_01.parquet")
    else:
        print("⚠️ No data returned.")
except requests.RequestException as e:
    print(f"❌ Request failed: {e}")
