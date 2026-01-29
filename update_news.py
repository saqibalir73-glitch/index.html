
  import requests
import json
from datetime import datetime

def fetch_news():
    # Yeh aik free rasta hai news lene ka
    url = "https://raw.githubusercontent.com/jamesrobertson/free-news-api/main/news.json"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Hum sirf top 10 news nikal rahe hain
            news_list = data[:10]
        else:
            raise Exception("API issue")
    except:
        # Agar API fail ho jaye toh ye dummy data chalay ga
        news_list = [
            {
                "title": "AI Revolution 2026",
                "description": "Artificial Intelligence is taking over the tech world rapidly.",
                "url": "https://google.com",
                "source": "Tech Daily",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
        ]

    # File mein save karna
    with open('news.json', 'w') as f:
        json.dump(news_list, f, indent=4)
    print("News updated successfully!")

if __name__ == "__main__":
    fetch_news()

