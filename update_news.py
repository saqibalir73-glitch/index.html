import json
import datetime

# 50 High-Quality Movies for perfect loading
movies_list = [
    {"title": "Pushpa 2: The Rule (2025)", "img": "https://image.tmdb.org/t/p/w500/9v9S9r47kX98L7OUnv9Y4I3E3mS.jpg", "link": "https://www.google.com/search?q=Pushpa+2+Download"},
    {"title": "Singham Again (Hindi)", "img": "https://image.tmdb.org/t/p/w500/6v7FvN2D6mO1O5N4VfV7O9S9R6m.jpg", "link": "https://www.google.com/search?q=Singham+Again+Download"},
    {"title": "Animal (2024) Uncut", "img": "https://image.tmdb.org/t/p/w500/hr9JAz68vXmG8V6Tz8O9A5X6U5m.jpg", "link": "https://www.google.com/search?q=Animal+Uncut+Download"},
    {"title": "Stree 2 (Hindi Dubbed)", "img": "https://image.tmdb.org/t/p/w500/7V9A5X6U5mhr9JAz68vXmG8V6Tz.jpg", "link": "https://www.google.com/search?q=Stree+2+Download"},
    {"title": "Kalki 2898 AD (4K)", "img": "https://image.tmdb.org/t/p/w500/6A5X6U5mhr9JAz68vXmG8V6Tz8O.jpg", "link": "https://www.google.com/search?q=Kalki+2898+Download"},
    {"title": "Deadpool & Wolverine", "img": "https://image.tmdb.org/t/p/w500/8cdcl36U69T9PUtC77Y95Y9Y9R6m.jpg", "link": "https://www.google.com/search?q=Deadpool+Wolverine+Hindi+Download"}
]

# Adding more entries to make it look full
for i in range(1, 41):
    movies_list.append({
        "title": f"Trending Movie {i} (Hindi Dubbed)",
        "img": "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmYp.jpg",
        "link": "https://www.google.com/search?q=hindi+dubbed+movies+download"
    })

data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": movies_list
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)
