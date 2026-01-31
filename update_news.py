import requests
import json
import os

# Google/TMDB API Connector
API_KEY = "138316d05242c6f75ef26cb3e316dd1d"

def fetch_auto_movies():
    # Trending aur Netflix Popular movies ka data
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&sort_by=popularity.desc&with_original_language=en|hi"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        movie_list = []
        for movie in data.get('results', []):
            movie_list.append({
                "id": str(movie['id']),
                "title": movie['title'],
                "year": movie['release_date'][:4] if movie.get('release_date') else "2026",
                "img": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                "desc": movie.get('overview', 'No description available.')[:100] + "..."
            })
        
        # News.json file ko update karna
        with open('news.json', 'w') as f:
            json.dump({"news_items": movie_list}, f, indent=4)
        print("Done: Google Data Connected!")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_auto_movies()
