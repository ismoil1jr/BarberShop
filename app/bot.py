# bot.py (yoki form ma'lumotlarini yuboradigan joy)

import requests

BOT_TOKEN = '8019622477:AAEI0HKjwE5KGiY4nc0sZ31JWubrI0-VaQ8'
CHAT_ID = '5690099705'

def send_telegram_message(name, phone, date, time):
    text = f"📥 Yangi appointment:\n\n👤 Ism: {name}\n📞 Tel: {phone}\n📅 Sana: {date}\n⏰ Vaqt: {time}"

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }

    response = requests.post(url, data=payload)
    print(response.json())
    return response.status_code == 200
