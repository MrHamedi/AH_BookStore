from django.contrib.sitemaps import Sitemap
from .models import Book 

class BooksSitemap(Sitemap):
	priority="0.8"
	chenge_freq="weekly"

	def items(self):
		return(Book.objects.all())

	def last_mod(self,obj):
		return(obj.update)
