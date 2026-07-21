import requests
import pandas as pd
# get rid of api key, normalize all columns on a scale 0-1, flip distance, add the weighted pieces to find the danger score
API_KEY = "YOUR_KEY_HERE"
url = "https://api.nasa.gov/neo/rest/v1/feed"
params = {
    "start_date": "2026-06-16",
    "end_date": "2026-06-23",
    "api_key": API_KEY
    }

response = requests.get(url, params=params)
neo = response.json()["near_earth_objects"]

rows = []
for date, asteroids in neo.items():
    for asteroid in asteroids:
        rows.append({
            "name": asteroid["name"],
            "date": date,
            "size_km": (asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_min"] + asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]) / 2,
            "speed_kmh": float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]),
            "miss_lunar": float(asteroid["close_approach_data"][0]["miss_distance"]["lunar"]),
            })
df = pd.DataFrame(rows)

df["size_norm"] = (df["size_km"] - df["size_km"].min()) / (df["size_km"].max() - df["size_km"].min())
df["speed_norm"] = (df["speed_kmh"] - df["speed_kmh"].min()) / (df["speed_kmh"].max() - df["speed_kmh"].min())
df["miss_norm"] = 1 - (df["miss_lunar"] - df["miss_lunar"].min()) / (df["miss_lunar"].max() - df["miss_lunar"].min())
df["danger"] = 0.4 * df["size_norm"] + 0.3 * df["speed_norm"] + 0.3 * df["miss_norm"]
df = df.sort_values("danger", ascending=False)
print(df)