#region imports
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.db import transaction
from django.contrib.auth.decorators import login_required
import django.views.generic as django_generic
from django.views.generic import TemplateView, DetailView

from .forms import UploadFileForm
from .models import Book, Chapter, Section, Line, TypedLineRecord

import re
#endregion

#region view methods and classes
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_list"] = Book.objects.all()
        return context

class TextTypeView(DetailView):
    model = Line
    template_name = 'get_text.html'

@login_required
def upload_booktext(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['document'], form.cleaned_data["name"])
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
#endregion

#region 'private' methods
def handle_uploaded_file(file, name):
    file.charset = 'UTF8'
    text = ''
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

