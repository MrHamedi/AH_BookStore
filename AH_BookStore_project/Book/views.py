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



@login_required(login_url="/accounts/login")
def send_book_view(request,book_slug):
	#This view will send book to client email
	book=get_object_or_404(Book,slug=book_slug)
	book_file=book.book.url[1:]
	email=request.user.email
	subject=f"Hi,You have asked for a book.Here it is for you.THank for using our service."
	message=EmailMessage(subject,"","AH Book Store",["ahmadihamed167@gmail.com",])
	message.content_subtype="pdf"
	message.attach_file(book_file)
	message.send()	
	return(HttpResponseRedirect(reverse("books:book_detail",args=[book.slug])))
	
