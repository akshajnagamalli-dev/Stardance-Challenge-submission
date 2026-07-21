# Stardance — Asteroid Radar

A Streamlit web app that tracks near-Earth asteroids and ranks them by a weighted "danger score."

## What it does
- Fetches 7 days of near-Earth-object data from NASA's NeoWs API
- Normalizes size, speed, and miss-distance onto a 0-1 scale
- Combines them into a danger score, weighted 0.4 size / 0.3 speed / 0.3 distance (size-heavy, since a large impactor is the bigger threat even from farther out)
- Displays a sorted danger table, a top-10 danger bar chart, and a per-asteroid detail view

## Running locally
1. Install dependencies: pip install -r requirements.txt
2. Add your NASA API key to .streamlit/secrets.toml as NASA_API_KEY = "your_key" (free key at https://api.nasa.gov)
3. Run: streamlit run app.py

## Built with
Python, Streamlit, pandas, Plotly, and the NASA NeoWs API.
