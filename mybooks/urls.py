from django.urls import path
from .views import *

urlpatterns = [
    path('', book_page),
    path('book/1', first_book),
    path('book/2', second_book),
    path('book/3', third_book),
    path('book/4', fourth_book),
]
