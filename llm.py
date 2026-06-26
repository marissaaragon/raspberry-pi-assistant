import requests
import config

def ask(prompt):
    payload = {
        "model": config.OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": config.SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    response = requests.post(config.OLLAMA_HOST + "/api/chat", json=payload)
    return response.json()["message"]["content"]

