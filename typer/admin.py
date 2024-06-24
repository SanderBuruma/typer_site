from django.contrib import admin

from .models import Book, Chapter, Section, Line, TypedLineRecord

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Section)
admin.site.register(Line)
admin.site.register(TypedLineRecord)
