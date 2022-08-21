from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

# Create your views here.

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
    with open('./temp.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            print(chunk)
    print(f'file uploaded: {file}')

