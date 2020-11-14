from django.db import models 
from django.urls import reverse
from datetime import datetime
from random import randrange
from django.urls import reverse

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



class Publisher(models.Model):
	name=models.CharField(max_length=300)
	About=models.TextField(blank=True)
	adress=models.TextField(blank=True)
	email=models.EmailField(blank=True)
	phone=models.CharField(max_length=11,blank=True)
	image=models.ImageField(upload_to=f"publishers/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/",null=True,blank=True)
	slug=models.SlugField(unique=True,max_length=200)

	def __str__(self):
		return(self.name)

	def slug_maker(self):
		return(f"Publisher/{self.name}")

subjects=(("EDU","Education"),("HiS","Historical"),("NOV","Novel"),("POE","Poem"),("MAG","Magazin"),("CHI","Childish"),("OTH","Others"))



class Book(models.Model):
	name=models.CharField(max_length=200)
	author=models.ManyToManyField(Author)
	publisher=models.ForeignKey(Publisher,on_delete=models.PROTECT,related_name="books")
	publish=models.DateField()
	description=models.TextField(blank=True)
	pages=models.BigIntegerField(blank=True)
	book_price=models.DecimalField(max_digits=5,decimal_places=1)
	image1=models.ImageField(upload_to=f"books/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/",null=True,blank=True)
	image2=models.ImageField(upload_to=f"books/{datetime.now().year}/{datetime.now().month}/{datetime.now().day}/",null=True,blank=True)
	offer_time=models.DateTimeField()
	slug=models.SlugField(max_length=200,unique=True)
	subject=models.CharField(max_length=100,choices=subjects,default="Others")

	class Meta:
		ordering=("-offer_time",)

	def authors_list(self):
		authors=self.author.all()
		return(authors)

	def slug_maker(self):
		return(f"Book/{self.author}/{self.name}/{self.publish}")
	
	def get_absolute_url(self):
		return(reverse("books:book_detail",args=[self.slug]))