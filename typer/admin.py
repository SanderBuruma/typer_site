from django.contrib import admin

from .models import Book, BookChapter, ChapterPart, PartLine, TypedLineRecord

admin.site.register(Book)
admin.site.register(BookChapter)
admin.site.register(ChapterPart)
admin.site.register(PartLine)
admin.site.register(TypedLineRecord)

