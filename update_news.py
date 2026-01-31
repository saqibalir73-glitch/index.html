import requests
import json
import datetime

# Aapki Master Key
API_KEY = "138316d05242c6f75ef26cb3e316dd1d"
BASE_URL = "https://api.themoviedb.org/3"

def get_movies():
    movies = []
    # Hum trending movies uthayenge taake posters asli hon
    url = f"{BASE_URL}/trending/movie/week?api_key={API_KEY}"
    response = requests.get(url).json()
    
    if 'results' in response:
        for i, res in enumerate(response['results'], 1):
            movies.append({
                "id": i,
                "title": res.get('title', 'No Title'),
                "img": f"https://image.tmdb.org/t/p/w500{res.get('poster_path')}",
                "year": res.get('release_date', '2025')[:4],
                "size_720": "1.4 GB",
                "desc": res.get('overview', 'No description available.'),
                "link": f"download.html?id={i}"
            })
    return movies

# Data update karna
movie_list = get_movies()
data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d"),
    "news_items": movie_list
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Mubarak ho! {len(movie_list)} movies asli posters ke saath update ho gayi hain.")
