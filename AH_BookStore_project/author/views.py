from .models import Author
from Book.models import Book
from django.shortcuts import render,get_object_or_404


def author_detail_view(request,id):
	author=get_object_or_404(Author,id=id)
	books=Book.objects.filter(author__id=id)
	return(render(request,"author/author_detail.html",{"author":author,"books":books}))
