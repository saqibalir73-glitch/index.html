import json
import datetime

titles = ["Pushpa 2", "Singham Again", "Animal", "Stree 2", "Kalki 2898 AD", "Jawan", "Pathaan", "Tiger 3", "Gadar 2", "Salaar"]
imgs = ["https://image.tmdb.org/t/p/w500/9v9S9r47kX98L7OUnv9Y4I3E3mS.jpg", "https://image.tmdb.org/t/p/w500/6v7FvN2D6mO1O5N4VfV7O9S9R6m.jpg", "https://image.tmdb.org/t/p/w500/hr9JAz68vXmG8V6Tz8O9A5X6U5m.jpg"]

movies = []
# Yeh loop 10,000 movies banayega
for i in range(1, 10001):
    m = titles[i % len(titles)]
    movies.append({
        "title": f"{m} (2026) Hindi Dubbed Full Movie HD",
        "img": imgs[i % len(imgs)],
        "link": f"/download-server-{i}.html"
    })

data = {"last_updated": datetime.datetime.now().strftime("%Y-%m-%d"), "news_items": movies}
with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)
