import requests
import json

def fetch_data():
    # Google/TMDB Database Connector
    url = "https://api.themoviedb.org/3/trending/movie/week?api_key=138316d05242c6f75ef26cb3e316dd1d"
    response = requests.get(url).json()
    movies = []
    
    for item in response.get('results', []):
        movies.append({
            "id": str(item['id']),
            "title": item['title'],
            "year": item['release_date'][:4] if item.get('release_date') else "2026",
            "img": f"https://image.tmdb.org/t/p/w500{item['poster_path']}"
        })
    
    with open('news.json', 'w') as f:
        json.dump({"news_items": movies}, f, indent=4)

if __name__ == "__main__":
    fetch_data()
