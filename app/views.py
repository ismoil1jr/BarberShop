from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Booking
from django.conf import settings
from telegram import Bot
from barber.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
import logging
import requests
from .bot import send_telegram_message  

# Loglashni sozlash
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from .bot import send_telegram_message  # yuqoridagi funksiyani shu faylga qo‘yilgan deb olamiz

def index(request):
    return render(request, 'index.html')

class BookingCreateView(CreateView):
    model = Booking
    fields = ['full_name', 'phone', 'booking_date', 'booking_time', 'number_of_people', 'message']
    template_name = 'index.html'
    success_url = reverse_lazy('index')

    def send_telegram_message(self, booking):
        token = '8019622477:AAEI0HKjwE5KGiY4nc0sZ31JWubrI0-VaQ8'
        chat_ids = [5690099705, 5500284042]  # Telegram chat ID larini o'zgartiring
        text = f"Yangi bron:\n\n" \
            f"Ism: {booking.full_name}\n" \
            f"Telefon: {booking.phone}\n" \
            f"Sana: {booking.booking_date}\n" \
            f"Vaqt: {booking.booking_time}\n" \
            f"Odamlar soni: {booking.number_of_people}\n" \
            f"Izoh: {booking.message or 'Yo‘q'}"

        for chat_id in chat_ids:
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {"chat_id": chat_id, "text": text}
            r = requests.post(url, data=payload)
            print(f"Telegram response: {r.json()}")
                # Xatolikni foydalanuvchiga ko'rsatmaslik kerak

    def form_valid(self, form):
        response = super().form_valid(form)
        booking = self.object
        print(f"✅ Booking saqlandi: {booking.full_name}")
        self.send_telegram_message(booking)
        return response



    def form_invalid(self, form):
        logger.error(f"Forma xatosi: {form.errors}")
        messages.error(self.request, "Forma to'ldirishda xatolik yuz berdi. Iltimos, ma'lumotlarni tekshiring.")
        return super().form_invalid(form)