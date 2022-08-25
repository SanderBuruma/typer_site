from django.db import models
from datetime import datetime
from django.utils import timezone

# region Text of the Book
class Book(models.Model):
    def __str__(self):
        return self.title
    title = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

class Chapter(models.Model):
    def __str__(self):
        return self.title
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.TextField()
    order = models.IntegerField(default=-1)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

class Section(models.Model):
    def __str__(self):
        return self.title
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.TextField()
    order = models.IntegerField(default=-1)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

class Line(models.Model):
    def __str__(self):
        return self.text[:50]
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(default=-1)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)
# endregion

# Player records
class TypedLineRecord(models.Model):
    line_fk = models.ForeignKey(Line, on_delete=models.CASCADE)
    seconds_taken = models.IntegerField(default=9999)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(default=timezone.now, blank=True)

