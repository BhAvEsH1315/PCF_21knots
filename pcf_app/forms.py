# pcf_app/forms.py
from django import forms

class MessageForm(forms.Form):
    product_name = forms.CharField(label='Product Name', max_length=255)
    carbon_footprint = forms.FloatField(label='Carbon Footprint')
    reference_start = forms.DateTimeField(label='Reference Start', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    reference_stop = forms.DateTimeField(label='Reference Stop', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
