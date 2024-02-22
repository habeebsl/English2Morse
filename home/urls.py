from django.urls import path
from .views import morse_code_conversion


urlpatterns = [
    path('', morse_code_conversion, name='home')
]