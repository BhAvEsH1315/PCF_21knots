# pcf_app/urls.py
from django.urls import path
from .views import MessageListCreateView, message_history

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('history/', message_history, name='message-history'),
]
