# pcf_app/urls.py
from django.urls import path
from .views import MessageListCreateView, message_history, message_form_view

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('history/', message_history, name='message-history'),
    path('message-form/', message_form_view, name='message-form'),
]
