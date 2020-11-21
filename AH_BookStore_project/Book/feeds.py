from django.contrib.syndication.views import Feed
from .models import Book
from django.urls import reverse_lazy

class BooksFeed(Feed):
	title="Book feed"
	link=reverse_lazy("books:homepage")
	descrption="This feed will return last three books that have been added"
	def items(self):
		return(Book.objects.all()[:3])
	def item_title(self,item):
		return(item.name)
	def item_descrption(self,item):
		return(item.description)