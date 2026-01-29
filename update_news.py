import json
def fetch_news():
    news_list = [{
        "title": "AI Revolution 2026",
        "description": "The AI era has officially begun. Your blog is now active!",
        "url": "https://google.com",
        "source": "Global AI Insights",
        "date": "2026-01-30"
    }]
    with open('news.json', 'w') as f:
        json.dump(news_list, f, indent=4)
fetch_news()
