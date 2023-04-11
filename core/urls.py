from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name='index'),
    path("book/",book_hall,name='book-hall'),

    path("login/",login_page,name='login'),
    path("logout/",logout_page,name='logout')
]