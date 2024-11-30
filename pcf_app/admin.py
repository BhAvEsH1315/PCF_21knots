# pcf_app/admin.py
from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'carbon_footprint', 'reference_start', 'reference_stop', 'timestamp')

admin.site.register(Message, MessageAdmin)
