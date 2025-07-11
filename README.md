# Chatbot

A simple chatbot built with LangGraph and Groq LLM integration.

## Features

- Interactive chat interface
- Uses Groq's Llama3-8b-8192 model
- Built with LangGraph for workflow management
- Simple command-line interface

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

3. Run the chatbot:
```bash
python3 Chatbot.py
```

## Usage

- Type your message and press Enter to chat
- Type "exit" to quit the chatbot

## Requirements

- Python 3.8+
- Groq API key
- Internet connection for API calls 