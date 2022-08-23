from django.db import models
from datetime import datetime

# region Text of the Book
class Book(models.Model):
    title = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class BookChapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.TextField()
    order = models.IntegerField(default=-1)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class ChapterPart(models.Model):
    chapter = models.ForeignKey(BookChapter, on_delete=models.CASCADE)
    title = models.TextField()
    order = models.IntegerField(default=-1)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

class PartLine(models.Model):
    part = models.ForeignKey(ChapterPart, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField(default=-1)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
# endregion

# Player records
class TypedLineRecord(models.Model):
    line_fk = models.ForeignKey(PartLine, on_delete=models.CASCADE)
    seconds_taken = models.IntegerField(default=9999)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

