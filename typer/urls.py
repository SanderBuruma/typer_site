from django.urls import path
from . import views
from typer.views import IndexView, TextTypeView

urlpatterns = [
    path('', IndexView.as_view()),
    path('text/<int:pk>', TextTypeView.as_view()),
    path('upload_booktext/', views.upload_booktext, name='upload_booktext'),
]

