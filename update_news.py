import json
import datetime

# Professional Data for Movies & Songs
data = {
    "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "news_items": [
        {"title": "Pathaan 2 - Official Teaser", "content": "SRK returns in the biggest action sequel of the decade.", "link": "https://www.youtube.com/results?search_query=pathaan+2+teaser"},
        {"title": "Latest Romantic Hit: Tu Kya Jaane", "content": "Diljit Dosanjh's new soulful track is trending everywhere.", "link": "https://www.youtube.com/results?search_query=tu+kya+jaane+diljit"},
        {"title": "Animal Park - Update", "content": "Ranbir Kapoor and Sandeep Reddy Vanga's next masterpiece details.", "link": "https://www.youtube.com/results?search_query=animal+park+movie"},
        {"title": "Top 10 Bollywood Songs 2026", "content": "Check out this week's most played music videos.", "link": "https://www.youtube.com/results?search_query=top+bollywood+songs+2026"},
        {"title": "Hollywood: Avengers Secret Wars", "content": "New leaks about the biggest Marvel movie of all time.", "link": "https://www.youtube.com/results?search_query=avengers+secret+wars"},
        {"title": "Heeramandi Season 2", "content": "Sanjay Leela Bhansali's epic saga continues on Netflix.", "link": "https://www.youtube.com/results?search_query=heeramandi+season+2"},
        {"title": "New Song: Tauba Tauba", "content": "Vicky Kaushal's dance moves are breaking the internet.", "link": "https://www.youtube.com/results?search_query=tauba+tauba+vicky+kaushal"},
        {"title": "War 2 - Shooting Leaks", "content": "Hrithik Roshan and Jr. NTR seen on the sets of War 2.", "link": "https://www.youtube.com/results?search_query=war+2+leaks"}
    ]
}

with open('news.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Robot Success: 8+ Premium Items Updated!")
