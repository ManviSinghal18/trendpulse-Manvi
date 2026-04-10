import json

# Load data
with open("data/top_trends.json", "r") as f:
    trends = json.load(f)

print("\n📊 FINAL INSIGHTS\n")

# Top trend
top_word, top_count = trends[0]
print(f"🔥 Most Trending Topic: {top_word} ({top_count} times)\n")

# Show all
print("📈 Top Trends:")
for word, count in trends:
    print(f"{word} → {count}")

# Final conclusion
print("\n💡 Conclusion:")
print("Most of the trending topics are related to AI and technology 🚀")