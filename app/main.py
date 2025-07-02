from app.chatbot import chat
import threading
import time

def background_research(session_id):
    """Arka planda sürekli araştırma yapar ve bilgileri kaydeder."""
    while True:
        chat("Arka planda araştırma yapıyorum.", session_id)
        time.sleep(300)  # Her 5 dakikada bir araştırma simülasyonu

def main():
    session_id = input("Lütfen bir oturum kimliği girin: ")
    print("Sohbete hoş geldiniz! Çıkmak için 'exit' yazın.")
    
    # Arka planda araştırma için thread başlat
    research_thread = threading.Thread(target=background_research, args=(session_id,), daemon=True)
    research_thread.start()
    
    while True:
        message = input("Siz: ")
        if message.lower() == "exit":
            break
        response = chat(message, session_id)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()