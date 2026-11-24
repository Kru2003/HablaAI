# 🇪🇸 HablaAI – AI-Powered Spanish Learning Application

HablaAI is a beginner-friendly, AI-powered Spanish learning application that acts as your personal Spanish tutor. It uses Google's Gemini API to provide interactive Spanish conversations, grammar corrections, vocabulary explanations, and personalized learning support.


## 📁 Project Structure

```text
HablaAI/
│
├── backend/
│   ├── .venv/                   # Python virtual environment
│   ├── .env                     # Environment variables
│   ├── requirements.txt         # Python dependencies
│   └── app/
│       ├── main.py              # FastAPI application
│       └── spanish_tutor.py     # Gemini-powered Spanish tutor
│
├── .gitignore                   # Git ignored files
└── README.md                    # Project documentation
```

## 📋 Prerequisites

Before running the project, make sure you have:

- Python 3.10 or higher
- pip (Python package manager)
- Google Gemini API key

Get your Gemini API key from:

https://aistudio.google.com/apikey

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/HablaAI.git
```

Navigate to the project directory:

```bash
cd HablaAI
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn google-genai
```

### 6. Configure Gemini API Key

Set your Gemini API key as an environment variable.

```bash
export GEMINI_API_KEY="your-api-key"
```

Replace `your-api-key` with your actual Gemini API key.

**Important:** Never share your API key or commit it to GitHub.

## ▶️ Running the Application

### 1. Start the Spanish Tutor

```bash
python spanish_tutor.py
```

You can now start chatting with HablaAI directly from your terminal.

Example:

```text
===================================
       Welcome to HablaAI
===================================
Your personal Spanish tutor
Type 'exit' to quit.

You: Hola, ¿cómo estás?

HablaAI: ¡Hola! Estoy muy bien, gracias.
¿Y tú? ¿Cómo estás?
```

Type `exit` or `quit` to end the conversation.

### 2. Start the FastAPI Backend

Run the following command:

```bash
uvicorn main:app --reload
```

The FastAPI server will start at:

http://127.0.0.1:8000

### Available API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/health` | Application health status |
| POST | `/chat` | Send a message to the AI Spanish tutor |
