import json
import datetime

titles = ["Pushpa 2", "Singham Again", "Animal", "Stree 2", "Kalki 2898 AD", "Jawan", "Pathaan", "Tiger 3", "Gadar 2", "Salaar"]
imgs = ["https://image.tmdb.org/t/p/w500/9v9S9r47kX98L7OUnv9Y4I3E3mS.jpg", "https://image.tmdb.org/t/p/w500/6v7FvN2D6mO1O5N4VfV7O9S9R6m.jpg", "https://image.tmdb.org/t/p/w500/hr9JAz68vXmG8V6Tz8O9A5X6U5m.jpg"]

movies = []
for i in range(1, 10001):
    m_name = titles[i % len(titles)]
    movies.append({
        "id": i,
        "title": f"{m_name} (2026) Official Hindi Dubbed HD",
        "img": imgs[i % len(imgs)],
        "year": "2026",
        "size_480": "450MB",
        "size_720": "1.2GB",
        "size_1080": "2.8GB",
        "desc": f"{m_name} is an upcoming Indian action thriller. Download in full HD original quality.",
        "link": f"download.html?id={i}" # Ye link aapki site ke download page par le jayega
    })

data = {"last_updated": datetime.datetime.now().strftime("%Y-%m-%d"), "news_items": movies}
with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)
