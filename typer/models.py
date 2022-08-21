from datetime import date
from django.db import models
from datetime import datetime

# Create your models here.

class BookText(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class TypedText(models.Model):
    book_text = models.ForeignKey(BookText, on_delete=models.CASCADE)
    seconds_taken = models.IntegerField(default=9999)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

