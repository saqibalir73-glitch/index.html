import json
def fetch_data():
    # News aur YouTube Videos ka data
    data = {
        "news": [{
            "title": "AI Trends 2026",
            "description": "Quantum computing and Agentic AI are ruling 2026.",
            "url": "https://google.com",
            "source": "Global AI Tech",
            "date": "2026-01-30"
        }],
        "videos": [{
            "title": "Top AI Trends 2026",
            "embed_url": "https://www.youtube.com/embed/zt0JA5rxdfM",
            "description": "Watch the latest breakthroughs."
        }]
    }
    with open('news.json', 'w') as f:
        json.dump(data, f, indent=4)
fetch_data()
