import json
import datetime

# Professional Movie List
movie_pool = [
    {"title": "Pushpa 2: The Rule", "img": "https://image.tmdb.org/t/p/w500/9v9S9r47kX98L7OUnv9Y4I3E3mS.jpg", "link": "https://www.google.com/search?q=Pushpa+2+Movie+Download"},
    {"title": "Singham Again", "img": "https://image.tmdb.org/t/p/w500/6v7FvN2D6mO1O5N4VfV7O9S9R6m.jpg", "link": "https://www.google.com/search?q=Singham+Again+Movie+Download"},
    {"title": "Animal (2024)", "img": "https://image.tmdb.org/t/p/w500/hr9JAz68vXmG8V6Tz8O9A5X6U5m.jpg", "link": "https://www.google.com/search?q=Animal+Movie+Download"},
    {"title": "Stree 2", "img": "https://image.tmdb.org/t/p/w500/7V9A5X6U5mhr9JAz68vXmG8V6Tz.jpg", "link": "https://www.google.com/search?q=Stree+2+Movie+Download"},
    {"title": "Kalki 2898 AD", "img": "https://image.tmdb.org/t/p/w500/6A5X6U5mhr9JAz68vXmG8V6Tz8O.jpg", "link": "https://www.google.com/search?q=Kalki+2898+AD+Movie+Download"}
]

# Robot data likh raha hai
data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": movie_pool
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)
