from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.


class Author(models.Model):
	name=models.CharField(max_length=200)
	About=models.TextField(blank=True)
	image=models.ImageField(upload_to=f"authors/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/",null=True,blank=True)
	slug=models.SlugField(unique=True,max_length=200)
	birthday=models.DateField()
	
	def __str__(self):
		return(self.name)

	def slug_maker(self):
		slug=f"Author/{self.name}+{self.birthay}"
		try:
			author=Author.objects.get(slug=slug)
			while(author):
				slug=f"Author/{self.name}/{self.birthay}/{randrange(1000000,9999999)}"
				author=Author.objects.get(slug=slug)

		except models.Model.DoesNotExist:
			return(slug)

	def get_absolute_url(self):
		return(reverse("author:author_detail",args=[self.slug]))