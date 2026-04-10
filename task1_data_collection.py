import requests
import json
from datetime import datetime
import os

categories = {
    "technology": ["ai", "software", "tech", "code", "data"],
    "worldnews": ["war", "government", "election", "global"],
    "sports": ["sport", "game", "team", "match"],
    "science": ["research", "study", "space", "science"],
    "entertainment": ["movie", "music", "show", "film"]
}

def get_category(title):
    title = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title:
                return category
    return "technology"  # default

headers = {"User-Agent": "TrendPulse/1.0"}

# Get top story IDs (reduced for speed)
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_ids = requests.get(top_url, headers=headers).json()[:150]

collected_data = []

for story_id in story_ids:
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        res = requests.get(url, headers=headers, timeout=5)

        if res.status_code != 200:
            continue

        data = res.json()
        if not data or "title" not in data:
            continue

        story = {
            "post_id": data.get("id"),
            "title": data.get("title"),
            "category": get_category(data["title"]),
            "score": data.get("score", 0),
            "num_comments": data.get("descendants", 0),
            "author": data.get("by"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected_data.append(story)

        # Stop after 110 stories (fast)
        if len(collected_data) >= 110:
            break

    except:
        continue

# Create folder
if not os.path.exists("data"):
    os.makedirs("data")

# Save file
filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4)

print(f"Collected {len(collected_data)} stories. Saved to {filename}")