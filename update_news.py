import urllib.request
import json
import datetime

# Aapki Master Key
API_KEY = "138316d05242c6f75ef26cb3e316dd1d"

def get_movies():
    movies = []
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key={API_KEY}"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            if 'results' in data:
                for i, res in enumerate(data['results'], 1):
                    movies.append({
                        "id": i,
                        "title": res.get('title', 'No Title'),
                        "img": f"https://image.tmdb.org/t/p/w500{res.get('poster_path')}",
                        "year": res.get('release_date', '2025')[:4],
                        "size_720": "1.4 GB",
                        "desc": res.get('overview', 'No description available.'),
                        "link": f"download.html?id={i}"
                    })
    except Exception as e:
        print(f"Error: {e}")
    return movies

movie_list = get_movies()
data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d"),
    "news_items": movie_list
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Success! {len(movie_list)} movies updated.")
