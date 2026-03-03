import requests
import schedule
import time
import os
from datetime import datetime

TOKEN = os.environ["TOKEN"]
CHAT_ID = -1002006235740
THREAD_ID = 128

def obtener_programacion():
    hoy = datetime.now().strftime("%d/%m/%Y")
    
    mensaje = f"📅 Programación deportiva - {hoy}\n\n"
    mensaje += "⚽ Fútbol\n"
    mensaje += "- Evento de ejemplo\n"
    mensaje += "  🕒 21:00\n"
    mensaje += "  📺 Movistar+\n\n"
    
    mensaje += "🏀 Baloncesto\n"
    mensaje += "- Evento de ejemplo\n"
    mensaje += "  🕒 20:30\n"
    mensaje += "  📺 DAZN\n"
    
    return mensaje

def enviar_mensaje():
    texto = obtener_programacion()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "message_thread_id": THREAD_ID,
        "text": texto
    }
    
    requests.post(url, data=payload)

schedule.every().day.at("08:00").do(enviar_mensaje)

print("Bot funcionando...")

while True:
    schedule.run_pending()
    time.sleep(60)
