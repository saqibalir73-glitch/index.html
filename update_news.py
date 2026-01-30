import json
import datetime

# Shuruat ke liye bade movies ke naam
seed_movies = ["Pushpa", "Animal", "Singham", "Jawan", "Pathaan", "Tiger", "Stree", "Kalki", "RRR", "KGF", "Drishyam", "Dangal", "War", "Leo", "Master", "Vikram", "Batman", "Spider-Man", "Avengers", "Joker"]
years = ["2023", "2024", "2025", "2026"]
qualities = ["HD", "4K", "Bluray", "Web-DL"]

all_items = []

# Loop jo 10,000 movies banayega
for i in range(1, 10001):
    m_name = seed_movies[i % len(seed_movies)]
    year = years[i % len(years)]
    quality = qualities[i % len(qualities)]
    
    all_items.append({
        "title": f"{m_name} Part {i} ({year}) {quality}",
        "img": f"https://image.tmdb.org/t/p/w500/8cdcl36U69T9PUtC77Y95Y9Y9R6m.jpg",
        "link": f"https://www.google.com/search?q={m_name}+full+movie+download+hindi"
    })

data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": all_items
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)

print("10,000 Movies Generated Successfully!")
