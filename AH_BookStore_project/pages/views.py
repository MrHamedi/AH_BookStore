from django.shortcuts import render 
from .models import Page 

def index_page_view(request,permalink):
	#achives the page by its permalink attribute
	page=Page.objects.get(permalink="/"+permalink)
	return(render(request,"pages/index.html",{"title":page.title,"content":page.content,}))