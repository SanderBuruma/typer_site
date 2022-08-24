#region imports
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import Book, Chapter, Section, Line, TypedLineRecord
from django.db import transaction
import re
#endregion

#region view methods
def index(request):
    return render(request, 'index.html')

def upload_booktext(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['document'])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
    
def get_text(request, id):
    arguments = {}
    if not Line.objects.filter(pk=id).exists():
        return HttpResponseRedirect("/")
    arguments['line'] = Line.objects.get(pk=id).text
    arguments['section'] = Line.objects.get(pk=id).section
    if Line.objects.filter(pk=id+1).exists():
        arguments['nextLine'] = Line.objects.get(pk=id+1).text
        arguments['nextLineId'] = id+1
    if Line.objects.filter(pk=id-1).exists():
        arguments['prevLine'] = Line.objects.get(pk=id-1).text
    return render(request, 'get_text.html', arguments)
#endregion

#region 'private' methods
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
    chapters, sections, lines = ([], [], [])
    orders = [1, 1, 1]
    for line in text:
        line = line[:-2]
        line = re.sub(r'[\\]', '', line)
        if '# ' == line[0:2]:
            chapters.append(Chapter(title=line[2:], order=orders[0], book=book))
            orders[0] += 1
            orders[1] = 1
            orders[2] = 1
        elif '## ' == line[0:3]:
            sections.append(Section(title=line[3:], order=orders[1], chapter=chapters[-1]))
            orders[1] += 1
            orders[2] = 1
        else:
            lines.append(Line(text=line, order=orders[2], section=sections[-1]))
            orders[2] += 1

    bulk_save(book, chapters, sections, lines)

def bulk_save(book, *args):
    book.save()
    for collection in args:
        for item in collection:
            item.save()

    transaction.commit()
#endregion
