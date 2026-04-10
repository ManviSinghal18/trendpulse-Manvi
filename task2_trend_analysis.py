import json
from collections import Counter
import re

# Load data
with open("data/trends_20260410.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract titles
titles = [story["title"] for story in data]

# Clean text function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

# Combine all words
all_words = []

for title in titles:
    cleaned = clean_text(title)
    words = cleaned.split()
    all_words.extend(words)

# Stopwords list
stopwords = [
    "the","is","in","and","to","of","for","on","with","a","an",
    "i","you","he","she","it","we","they","my","your","our",
    "this","that","these","those",
    "am","are","was","were","be","been","being",
    "have","has","had","do","does","did",
    "but","if","or","because","as","until","while",
    "how","what","when","where","why",
    "hn","ok","yes","no",
    "show","code","new","testing","over","us","c"
]

# Remove stopwords
filtered_words = [word for word in all_words if word not in stopwords]

# Remove small/noisy words
filtered_words = [word for word in filtered_words if len(word) > 2 or word == "ai"]

# Count frequency
word_counts = Counter(filtered_words)

# Top 10 trends
top_trends = word_counts.most_common(10)

# Print results
print("🔥 Top Trending Words:\n")
for word, count in top_trends:
    print(f"{word} → {count}")

# Save to JSON
with open("data/top_trends.json", "w") as f:
    json.dump(top_trends, f)