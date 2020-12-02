from django.views.generic.list import ListView 
from Book.models import Book
from django.shortcuts import render,get_object_or_404 
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage


class BookListView(ListView):
	model=Book 
	paginate_by=3
	template_name="book/homepage.html"
	context_object_name="books"


def book_detail_view(request,book_slug):
	book=get_object_or_404(Book,slug=book_slug)
	return(render(request,"book/book_detail.html",{"book":book}))

