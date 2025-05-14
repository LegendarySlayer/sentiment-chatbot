import matplotlib.pyplot as plt

# Sample response distribution
emotion_counts = {
    'joy': 18,
    'sadness': 12,
    'anger': 9,
    'admiration': 14,
    'neutral': 7
}

labels = list(emotion_counts.keys())
counts = list(emotion_counts.values())

plt.figure(figsize=(7, 5))
plt.barh(labels, counts, color='coral')
plt.title("Number of Responses per Emotion Category")
plt.xlabel("Number of Responses")
plt.grid(axis='x', linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
