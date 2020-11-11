from django.db import models 
from django.urls import reverse

class Author(models.Model):
	name=models.CharField(max_length=200)
	About=models.TextField(blank=True)
	image=models.ImageField(upload_to="media/authors/Y/m/d/",null=True)
	slug=models.SlugField(unique=True,max_length=200)

	def __str__(self):
		return(self.name)


class Publisher(models.Model):
	name=models.CharField(max_length=300)
	About=models.TextField()
	adress=models.TextField()
	email=models.EmailField(blank=True)
	phone=models.CharField(max_length=11)
	image=models.ImageField(upload_to="media/publishers/Y/m/d/",null=True)
	slug=models.SlugField(unique=True,max_length=200)

	def __str__(self):
		return(self.name)

subjects=(("EDU","Education"),("HiS","Historical"),("NOV","Novel"),("POE","Poem"),("MAG","Magazin"),("CHI","Childish"),("OTH","Others"))



class Book(models.Model):
	name=models.CharField(max_length=200)
	author=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Publisher,name="books",on_delete=models.PROTECT)
	publish=models.DateField()
	description=models.TextField()
	pages=models.IntegerField()
	price=models.DecimalField(max_digits=5,decimal_places=1)
	image1=models.ImageField(upload_to="media/books/Y/m/d/",null=True)
	image2=models.ImageField(,null=True)
	offer_time=models.DateTimeField()
	slug=models.SlugField(max_length=200,unique=True)
	subject=models.CharField(max_length=100,choices=subjects,default="Others")

	class Meta:
		ordering("-offer_time")
