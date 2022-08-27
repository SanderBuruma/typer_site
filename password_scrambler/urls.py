from django.urls import path
from . import views

urlpatterns = [
    path('password/get', views.get_password, name='get_password'),
    path('password/get/<int:password_length>', views.get_password, name='get_password'),
    path('password/get/<int:password_length>/<int:number_chars>', views.get_password, name='get_password'),
    path('password/get/<int:password_length>/<int:number_chars>/<int:special_chars>', views.get_password, name='get_password'),
    path('password/check/<int:id>', views.check_password, name='check_password'),
]