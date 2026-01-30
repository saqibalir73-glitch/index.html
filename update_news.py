import json
import datetime

# Naya data: Bollywood Songs aur World Movies ki list
data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": [
        {
            "title": "Latest Bollywood Hit 2026",
            "content": "Check out the top trending Bollywood song of the week. Full music video now streaming!",
            "link": "https://www.youtube.com/results?search_query=bollywood+songs+2026"
        },
        {
            "title": "Hollywood Blockbuster Trailer",
            "content": "Experience the thrill of the latest world cinema release. Watch the official movie trailer here.",
            "link": "https://www.youtube.com/results?search_query=world+movie+trailers+2026"
        }
    ]
}

# news.json file ko update karna
with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Robot Success: Bollywood and Movie data updated!")
