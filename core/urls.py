from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("book/",book_hall,name='book-hall')
]