from django.urls import path
from .views import home, me, contact

urlpatterns = [
    path("", home),
    path("home", home),
    path("me", me),
    path("contact", contact),
]
