from django.shortcuts import render,get_object_or_404
from .models import Publisher 
from Book.models import Book
# Create your views here.

def publisher_detail_view(request,id):
	publisher=get_object_or_404(Publisher,id=id)
	books=Book.objects.filter(publisher__id=id)
	return(render(request,"publisher/publisher_detail.html",{"publisher":publisher,"books":books}))