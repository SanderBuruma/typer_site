from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

# Create your models here.
class Password(models.Model):
    def __str__(self):
        return self.title

    password = models.CharField(max_length=128, default="")

    @property
    def shuffled(self):
        return random.shuffle(self.password)

    user = models.ForeignKey(User)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
