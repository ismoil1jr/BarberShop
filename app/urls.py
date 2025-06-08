from django.urls import path
from .views import BookingCreateView, index


urlpatterns = [
    path('', index, name='index'),
    path('booking/', BookingCreateView.as_view(), name='booking'),
]