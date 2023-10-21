from .consumers import ChatConsumer
from django.urls import path


websocket_urlpatterns = [
    path("ws/socket", ChatConsumer.as_asgi())
]