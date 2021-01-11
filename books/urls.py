from django.contrib import admin
from django.urls import path, include
from .views import BooksListView, BookDetailsView

urlpatterns = [
    path('', BooksListView.as_view(), name='books'),
    path('<int:pk>/', BookDetailsView.as_view(), name='book_details'),
]
