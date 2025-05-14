import matplotlib.pyplot as plt

# Sample emotions and their confidence scores
emotions = ['joy', 'sadness', 'anger', 'admiration', 'neutral']
confidence_scores = [0.82, 0.70, 0.76, 0.94, 0.65]

plt.figure(figsize=(8, 5))
plt.bar(emotions, confidence_scores, color='skyblue')
plt.title("Confidence Scores for Sample Emotions")
plt.xlabel("Emotions")
plt.ylabel("Confidence Score")
plt.ylim(0, 1)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
