from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from random import sample
class ScrambledPassword(models.Model):
    def __str__(self):
        return self.text

    text = models.CharField(max_length=128, default="")

    @property
    def shuffled(self):
        return ''.join(sample(self.text,len(self.text)))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
