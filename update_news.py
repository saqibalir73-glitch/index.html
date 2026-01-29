import feedparser

def fetch_and_update():
    # Google News se AI ki khabrein nikalna
    feed = feedparser.parse("https://news.google.com/rss/search?q=artificial+intelligence")
    news_html = ""
    
    # Top 5 news cards banana
    for entry in feed.entries[:5]:
        news_html += f'<div class="card"><h2>{entry.title}</h2><p>Latest AI update.</p><a href="{entry.link}" class="btn" target="_blank">Read More</a></div>'

    # index.html ko read karna
    with open("index.html", "r") as f:
        data = f.read()

    # Container ke andar news insert karna
    start_marker = '<div class="container">'
    end_marker = '</div>'
    
    parts = data.split(start_marker)
    if len(parts) > 1:
        after_container = parts[1].split(end_marker)
        new_data = parts[0] + start_marker + news_html + end_marker + after_container[-1]
        
        with open("index.html", "w") as f:
            f.write(new_data)

if __name__ == "__main__":
    fetch_and_update()
  
