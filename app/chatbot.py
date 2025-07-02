from app.memory import load_conversation, save_conversation
from app.research import perform_research
from app.code_generator import generate_code
import re

def detect_intent(message):
    """Kullanıcının niyetini algılar."""
    if re.search(r"(kod|fonksiyon|script)\s+(yaz|oluştur|generate)", message, re.IGNORECASE):
        return "code_generation"
    elif re.search(r"(nedir|açıklama|bilgi|nasıl|niçin)", message, re.IGNORECASE):
        return "research"
    else:
        return "general"

def chat(message, session_id):
    """Mesajı işler ve yanıt üretir."""
    history = load_conversation(session_id)
    history.append({"user": message})
    
    intent = detect_intent(message)
    if intent == "code_generation":
        match = re.search(r"(kod|fonksiyon|script)\s+(yaz|oluştur|generate)\s+(.+)", message, re.IGNORECASE)
        if match:
            task = match.group(3).strip()
            response = generate_code(task)
        else:
            response = "Kod talebinizi anlamadım."
    elif intent == "research":
        response = perform_research(message)
        # Araştırma sonucunu kaydet
        history.append({"research": response})
    else:
        response = "Size nasıl yardımcı olabilirim?"
    
    history.append({"bot": response})
    save_conversation(session_id, history)
    return response