from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Book, BookChapter, ChapterPart, PartLine, TypedLineRecord
from django.db import transaction

def index(request):
    return HttpResponse("This is the typer website!")

def upload_booktext(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['document'])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(file):
    file.charset = 'UTF8'
    count = 0
    text = '';
    for chunk in file.chunks():
        count += 1
        text += str(chunk)
    text = text.split('\\n')
    text[0] = text[0][2:]
    book = Book(title=file.name)
    chapters, parts, lines = ([], [], [])
    orders = [1, 1, 1]
    for line in text:
        if '# ' == line[0:2]:
            chapters.append(BookChapter(title=line[2:], order=orders[0], book=book))
            orders[0] += 1
            orders[1] = 1
            orders[2] = 1
        elif '## ' == line[0:3]:
            parts.append(ChapterPart(title=line[3:], order=orders[1], chapter=chapters[-1]))
            orders[1] += 1
            orders[2] = 1
        else:
            lines.append(PartLine(text=line, order=orders[2], part=parts[-1]))
            orders[2] += 1

    bulk_save(book, chapters, parts, lines)

# @transaction.atomic
def bulk_save(book, *args):
    book.save()
    for collection in args:
        for item in collection:
            item.save()

    transaction.commit()
