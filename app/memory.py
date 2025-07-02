import json
import os

DATA_DIR = "data"
CONVERSATIONS_FILE = os.path.join(DATA_DIR, "conversations.json")

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_conversation(session_id):
    """Belirtilen oturumun konuşma geçmişini yükler."""
    try:
        if not os.path.exists(CONVERSATIONS_FILE):
            return []
        with open(CONVERSATIONS_FILE, "r") as f:
            data = json.load(f)
            return data.get(session_id, [])
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_conversation(session_id, history):
    """Konuşma geçmişini kaydeder."""
    try:
        if not os.path.exists(CONVERSATIONS_FILE):
            data = {}
        else:
            with open(CONVERSATIONS_FILE, "r") as f:
                data = json.load(f)
        data[session_id] = history
        with open(CONVERSATIONS_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except (json.JSONDecodeError, FileNotFoundError):
        with open(CONVERSATIONS_FILE, "w") as f:
            json.dump({session_id: history}, f, indent=4)