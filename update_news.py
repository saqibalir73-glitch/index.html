import requests, json

# TMDB se connect kar raha hai (Netflix/Filmyzilla data ke liye)
def fetch_movies():
    url = "https://api.themoviedb.org/3/trending/movie/week?api_key=138316d05242c6f75ef26cb3e316dd1d"
    data = requests.get(url).json()
    movies = []
    for m in data.get('results', []):
        movies.append({
            "id": str(m['id']),
            "title": m['title'],
            "year": m['release_date'][:4] if m.get('release_date') else "2026",
            "img": f"https://image.tmdb.org/t/p/w500{m['poster_path']}"
        })
    with open('news.json', 'w') as f:
        json.dump({"news_items": movies}, f, indent=4)

if __name__ == "__main__":
    fetch_movies()
