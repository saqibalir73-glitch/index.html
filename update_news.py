import json
def fetch_news():
    # Yeh data website par nazar aayega
    news_list = [{
        "title": "AI Revolution 2026",
        "description": "Your AI portal is now live with YouTube integration!",
        "url": "https://google.com",
        "source": "System Update",
        "date": "2026-01-30"
    }]
    with open('news.json', 'w') as f:
        json.dump(news_list, f, indent=4)
fetch_news()
