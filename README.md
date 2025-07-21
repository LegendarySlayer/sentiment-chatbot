# 🤖 Emotion-Aware Chatbot

This is a Python-based emotion-aware chatbot that uses a fine-tuned [GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions) model to detect user emotions and respond empathetically using the OpenRouter API.

## 🚀 Features

- Detects 28 different emotions using a custom fine-tuned model
- Provides contextual and empathetic responses via Mixtral-8x7B
- Console-based interaction loop

## 🛠️ Setup

1. Clone the repository or unzip the folder.
2. Place your fine-tuned model folder as `finetuned_optimized_goemotions` in the root.
3. Replace `API_KEY` in `chatbot.py` with your OpenRouter API key.
4. Login to [Weights & Biases](https://wandb.ai/) using the command below and provide your API key:

```bash
wandb login YOUR_WANDB_API_KEY
```

## 📦 Requirements

Install the necessary packages with:

```bash
pip install -r requirements.txt
```

## 🧪 Run

```bash
python chatbot.py
```

## 📂 Folder Structure

```
EmotionChatbot/
├── chatbot.py
├── requirements.txt
├── README.md
└── finetuned_optimized_goemotions/  <- Place your model files here
```

---

💡 *Note: We assumes your model files (config.json, tokenizer, pytorch_model.bin etc.) are already available.*
---

Collaborators:

GitHub: [@Hayzzy](https://github.com/Strookee)
GitHub: [@Hayzzy](https://github.com/Brototee)
GitHub: [@Hayzzy](https://github.com/sanyasingh09)
GitHub: [@Hayzzy](https://github.com/Utkarsh-Jha171)
GitHub: [@Hayzzy](https://github.com/LegendarySlayer)
