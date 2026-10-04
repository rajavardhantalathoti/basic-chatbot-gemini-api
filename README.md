# 🤖 Basic Chatbot using Gemini LLM API

A simple terminal-based AI chatbot built with Python and Google's Gemini API (Free Tier).

---

## 🚀 Features

- 💬 Multi-turn conversation (the bot **remembers** previous messages)
- 🔒 Secure API key management using `.env`
- ⚡ Powered by **Gemini 2.0 Flash** (Google's free tier model)
- 🛡️ Error handling for network/API issues
- 🧹 Clean terminal UI

---

## 🗂️ Project Structure

```
📁 Basic chat bot using llm api calls/
│
├── 📄 chatbot.py          ← Main chatbot Python code
├── 📄 requirements.txt    ← Python dependencies
├── 📄 .env                ← Your secret API key (NOT uploaded to GitHub)
├── 📄 .gitignore          ← Prevents .env from being pushed to GitHub
└── 📄 README.md           ← You are here!
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8 or higher installed
- A Google account (to get the free API key)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### Step 2 — Create & Activate Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Get Your Free Gemini API Key

1. Go to 👉 [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the generated key

### Step 5 — Add Your API Key

Create a `.env` file in the project root:

```
GEMINI_API_KEY=paste_your_api_key_here
```

> ⚠️ **Never share your API key or push it to GitHub!**

### Step 6 — Run the Chatbot

```bash
python chatbot.py
```

---

## 🆓 Gemini Free Tier Limits

| Limit | Value |
|---|---|
| Requests per minute | 15 |
| Tokens per day | 1,000,000 |
| Cost | **FREE** |

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `google-genai` | Google's official Gemini SDK |
| `python-dotenv` | Loads API key from `.env` file securely |

---

## 🛠️ Troubleshooting

| Error | Fix |
|---|---|
| `GEMINI_API_KEY not found` | Make sure `.env` file exists with correct key |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` inside venv |
| Quota exceeded | Wait a minute — free tier allows 15 requests/min |

---

## 🙌 Support

If this helped you, please ⭐ **star this repository!**
