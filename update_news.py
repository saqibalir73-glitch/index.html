import json
import datetime

# 500+ Movies Database (Sample Pattern)
movies_list = []
titles = ["Pushpa 2", "Singham Again", "Animal", "Stree 2", "Jawan", "Pathaan", "Tiger 3", "KGF 2", "RRR", "Salaar"]

for i in range(1, 501):
    name = titles[i % len(titles)]
    movies_list.append({
        "title": f"{name} Part {i} (Hindi Dubbed)",
        "img": "https://image.tmdb.org/t/p/w500/8cdcl36U69T9PUtC77Y95Y9Y9R6m.jpg",
        "link": f"https://www.google.com/search?q={name.replace(' ', '+')}+download"
    })

data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": movies_list
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)
