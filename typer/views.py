#region imports
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import UploadFileForm
from .models import Book, Chapter, Section, Line, TypedLineRecord

import re
#endregion

#region view methods
def index(request):
    arguments = {}
    arguments['first_lines'] = get_first_lines()
    return render(request, 'index.html', arguments)

@login_required
def upload_booktext(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['document'], form.cleaned_data["name"])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
    
def get_text(request, id):
    arguments = {}
    if not Line.objects.filter(pk=id).exists():
        return HttpResponseRedirect("/")
    line = Line.objects.get(pk=id)
    arguments['line'] = Line.objects.get(pk=id).text
    arguments['section'] = Line.objects.get(pk=id).section
    if Line.objects.filter(pk=id+1, section__chapter__book_id=line.section.chapter.book.id).exists():
        arguments['nextLine'] = Line.objects.get(pk=id+1).text
        arguments['nextLineId'] = id+1
    if Line.objects.filter(pk=id-1, section__chapter__book_id=line.section.chapter.book.id).exists():
        arguments['prevLine'] = Line.objects.get(pk=id-1).text
        arguments['prevLineId'] = id-1
    return render(request, 'get_text.html', arguments)
#endregion

#region 'private' methods
def handle_uploaded_file(file, name):
    file.charset = 'UTF8'
    text = '';
    for chunk in file.chunks():
        text += str(chunk)
    text = text.split('\\n')
    text[0] = text[0][2:]
    book = Book(title=name)
    chapters, sections, lines = ([], [], [])
    orders = [1, 1, 1]
    for line in text:
        line = re.sub(r'[\r\n]', '', line)
        line = re.sub(r'\\[rn]', '', line)
        line = re.sub(r'[\\]', '', line)
        line = re.sub(r'^[^#]*?(?=# )', '', line)
        line = re.sub(r'^[^#]*?(?=## )', '', line)
        if '## ' in line:
            sections.append(Section(title=line[3:], order=orders[1], chapter=chapters[-1]))
            orders[1] += 1
            orders[2] = 1
        elif '# ' in line:
            chapters.append(Chapter(title=line[2:], order=orders[0], book=book))
            orders[0] += 1
            orders[1] = 1
            orders[2] = 1
        else:
            try: 
                lines.append(Line(text=line, order=orders[2], section=sections[-1]))
            except:
                print()
            orders[2] += 1

    bulk_save(book, chapters, sections, lines)

@transaction.atomic
def bulk_save(book, *args):
    book.save()
    for collection in args:
        for item in collection:
            item.save()


def get_first_lines():
    # the first line of each book
    first_lines = Line.objects.filter(section__chapter__order=1, section__order=1, order=1).all()
    return first_lines
#endregion

