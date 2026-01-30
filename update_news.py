import json
import datetime
import requests

# Hum trending Bollywood aur Hollywood movies uthayenge
def get_trending_movies():
    # Note: Filhal main 30-40 trending movies ka setup de raha hoon
    # Taake aapki site bhari hui lage
    movies = [
        "Pushpa 2 The Rule", "Singham Again", "Animal 2024", "Stree 2", 
        "Kalki 2898 AD", "Jawan", "Pathaan", "Salaar", "Leo Hindi Dubbed",
        "Deadpool and Wolverine Hindi", "Avatar 2 Hindi", "Spider-Man No Way Home Hindi",
        "KGF Chapter 2", "RRR", "Kantaram", "Drishyam 2", "War", "Tiger 3"
    ]
    
    items = []
    for m in movies:
        items.append({
            "title": m,
            "content": f"Watch {m} Full Movie in HD Hindi Dubbed. High Speed Download Links Available.",
            "link": f"https://www.google.com/search?q={m.replace(' ', '+')}+full+movie+download+hindi+dubbed"
        })
    return items

data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": get_trending_movies()
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)
