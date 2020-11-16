from django.urls import path 
from .views import BookListView,book_detail_view

app_name="books"

urlpatterns = [
	path("",BookListView.as_view(),name="homepage"),
	path("<slug:book_slug>/",book_detail_view,name="book_detail"),
]