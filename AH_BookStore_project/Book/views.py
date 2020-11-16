from django.views.generic.list import ListView 
from Book.models import Book
from django.shortcuts import render,get_object_or_404 


class BookListView(ListView):
	model=Book 
	paginate_by=3
	template_name="book/homepage.html"
	context_object_name="books"


def book_detail_view(request,book_slug):
	book=get_object_or_404(Book,slug=book_slug)
	return(render(request,"book/book_detail.html",{"book":book}))