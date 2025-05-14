# chatbot.py

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import requests
import json

# ✅ Load model from local path (adjust this if you're not using Colab)
model_path = "finetuned_optimized_goemotions"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

emotion_label_mapping = {
    0: "admiration", 1: "amusement", 2: "anger", 3: "annoyance", 4: "approval",
    5: "caring", 6: "confusion", 7: "curiosity", 8: "desire", 9: "disappointment",
    10: "disapproval", 11: "disgust", 12: "embarrassment", 13: "excitement",
    14: "fear", 15: "gratitude", 16: "grief", 17: "joy", 18: "love", 19: "nervousness",
    20: "optimism", 21: "pride", 22: "realization", 23: "relief", 24: "remorse",
    25: "sadness", 26: "surprise", 27: "neutral"
}

def detect_emotion(text):
    result = classifier(text)[0]
    label_index = int(result["label"].split("_")[-1]) if result["label"].startswith("LABEL_") else 27
    emotion = emotion_label_mapping.get(label_index, "neutral")
    confidence = result["score"]
    return emotion, confidence

API_KEY = "sk-or-REPLACE_WITH_YOUR_API_KEY"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def groq_reply(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a friendly emotional support chatbot."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(BASE_URL, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠️ Error: {response.status_code} - {response.text}"

def chat():
    print("🤖 Chatbot: Hi! How are you feeling today? (Say 'exit' to quit)")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("👋 Bye!")
                break

            emotion, confidence = detect_emotion(user_input)
            print(f"🧠 Emotion Detected: {emotion}")
            print(f"📊 Confidence Score: {confidence:.4f}")

            prompt = f"The user said: '{user_input}'. They are feeling {emotion}. Respond empathetically and helpfully."
            reply = groq_reply(prompt)
            print("🤖 Chatbot:", reply)
            print("-" * 120)

        except KeyboardInterrupt:
            print("
👋 Chat ended.")
            break

# ✅ Run the chatbot
if __name__ == "__main__":
    chat()