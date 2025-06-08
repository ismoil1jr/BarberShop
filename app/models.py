from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    # Faqat raqamlarni tekshirish (9 yoki 12 belgidan iborat)
    if not (re.match(r'^\+998[0-9]{9}$', value) or re.match(r'^[0-9]{9}$', value)):
        raise ValidationError('Telefon raqami 9 ta raqamdan iborat bo‘lishi kerak (masalan, 995554477) yoki +998 bilan boshlanishi mumkin.')

class Booking(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Ism va familiya")
    phone = models.CharField(
        max_length=12,
        verbose_name="Telefon raqami",
        help_text="9 ta raqam (masalan, 995554477) yoki +998XX-XXX-XX-XX",
        validators=[validate_phone_number]
    )
    booking_date = models.DateField(verbose_name="Bron sanasi")
    booking_time = models.TimeField(verbose_name="Bron vaqti")
    number_of_people = models.PositiveIntegerField(verbose_name="Odamlar soni")
    message = models.TextField(blank=True, verbose_name="Qo'shimcha izoh")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Bron"
        verbose_name_plural = "Bronlar"

    def __str__(self):
        return f"{self.full_name} - {self.booking_date} {self.booking_time}"