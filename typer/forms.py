from django import forms

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    name = forms.CharField(label="Name", max_length=100)
    document = forms.FileField()

