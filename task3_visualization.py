import json
import matplotlib.pyplot as plt

# Load trends
with open("data/top_trends.json", "r") as f:
    trends = json.load(f)

# Separate words and counts
words = [item[0] for item in trends]
counts = [item[1] for item in trends]

# Plot graph
plt.figure()
plt.bar(words, counts)

# Labels
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top Trending Topics")

# Rotate labels
plt.xticks(rotation=45)

# Save graph image
plt.savefig("data/trend_graph.png")

# Show graph
plt.show()