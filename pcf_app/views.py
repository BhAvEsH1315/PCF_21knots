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
