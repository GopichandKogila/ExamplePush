from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('author', views.createAuthor, name='author'),
    path('book', views.createBook, name='book'),
] 

