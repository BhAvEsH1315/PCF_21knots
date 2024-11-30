# pcf_app/models.py
from django.db import models

class Message(models.Model):
    product_name = models.CharField(max_length=255)
    carbon_footprint = models.FloatField()
    reference_start = models.DateTimeField()
    reference_stop = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
