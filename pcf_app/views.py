# pcf_app/views.py
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
import jsonschema
from jsonschema import validate, ValidationError
from rest_framework.response import Response

# Define the PCF schema
PCF_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "PCF Data Exchange Format",
    "type": "object",
    "properties": {
        "product_name": {"type": "string"},
        "carbon_footprint": {"type": "number"},
        "reference_start": {"type": "string", "format": "date-time"},
        "reference_stop": {"type": "string", "format": "date-time"}
    },
    "required": ["product_name", "carbon_footprint", "reference_start", "reference_stop"]
}

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        try:
            validate(instance=request.data, schema=PCF_SCHEMA)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)
        return self.create(request, *args, **kwargs)

# pcf_app/views.py
from django.shortcuts import render
from .models import Message

def message_history(request):
    messages = Message.objects.all()
    return render(request, 'message_history.html', {'messages': messages})

# pcf_app/views.py
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Message
import pytz

def message_form_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            carbon_footprint = form.cleaned_data['carbon_footprint']
            reference_start = form.cleaned_data['reference_start']
            reference_stop = form.cleaned_data['reference_stop']

            # Adjust the timestamps to the local timezone
            timezone = pytz.timezone('Asia/Kolkata')
            reference_start = reference_start.astimezone(timezone)
            reference_stop = reference_stop.astimezone(timezone)

            # Save the data to the database
            Message.objects.create(
                product_name=product_name,
                carbon_footprint=carbon_footprint,
                reference_start=reference_start,
                reference_stop=reference_stop
            )
            return redirect('message-form')  # Redirect to the same form page or another page
    else:
        form = MessageForm()

    return render(request, 'message_form.html', {'form': form})
