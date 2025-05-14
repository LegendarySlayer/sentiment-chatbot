import matplotlib.pyplot as plt

# Simulated accuracy over 20 epochs
epochs = list(range(1, 21))
accuracy = [round(0.7 + 0.015*i + (0.01 if i%5 == 0 else 0), 4) for i in range(20)]

plt.figure(figsize=(8, 5))
plt.plot(epochs, accuracy, marker='o', color='green')
plt.title("Model Accuracy Over Epochs")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.ylim(0.6, 1.0)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
