import json
import datetime

# Professional Movie Database
movies = [
    {"title": "Pushpa 2: The Rule (2025)", "img": "https://image.tmdb.org/t/p/w500/9v9S9r47kX98L7OUnv9Y4I3E3mS.jpg", "link": "https://www.google.com/search?q=Pushpa+2+Full+Movie+Download"},
    {"title": "Singham Again (Hindi)", "img": "https://image.tmdb.org/t/p/w500/6v7FvN2D6mO1O5N4VfV7O9S9R6m.jpg", "link": "https://www.google.com/search?q=Singham+Again+Full+Movie+Download"},
    {"title": "Animal (2024) Uncut", "img": "https://image.tmdb.org/t/p/w500/hr9JAz68vXmG8V6Tz8O9A5X6U5m.jpg", "link": "https://www.google.com/search?q=Animal+Uncut+Download"},
    {"title": "Stree 2 (Hindi Dubbed)", "img": "https://image.tmdb.org/t/p/w500/7V9A5X6U5mhr9JAz68vXmG8V6Tz.jpg", "link": "https://www.google.com/search?q=Stree+2+Full+Movie+Download"},
    {"title": "Kalki 2898 AD (4K)", "img": "https://image.tmdb.org/t/p/w500/6A5X6U5mhr9JAz68vXmG8V6Tz8O.jpg", "link": "https://www.google.com/search?q=Kalki+2898+AD+Full+Movie+Download"},
    {"title": "Deadpool & Wolverine", "img": "https://image.tmdb.org/t/p/w500/8cdcl36U69T9PUtC77Y95Y9Y9R6m.jpg", "link": "https://www.google.com/search?q=Deadpool+Wolverine+Hindi+Download"}
]

data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": movies
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)
