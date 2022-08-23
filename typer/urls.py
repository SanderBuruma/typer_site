from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_booktext/', views.upload_booktext, name='upload_booktext'),
    path('text/<int:id>', views.get_text, name='get_text'),
]

