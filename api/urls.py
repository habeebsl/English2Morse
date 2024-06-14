from django.urls import path
from .views import api_translator


urlpatterns = [
    path("", api_translator, name="api"),
]