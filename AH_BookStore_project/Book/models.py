from django.db import models 
from author.models import Author 
from publisher.models import Publisher
from django.urls import reverse
from datetime import datetime
from random import randrange
from django.urls import reverse

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
	update=models.DateTimeField(auto_now=True,null=True)
	book=models.FileField(null=True)

	class Meta:
		ordering=("-offer_time",)

	def authors_list(self):
		authors=self.author.all()
		return(authors)

	def slug_maker(self):
		return(f"Book/{self.author}/{self.name}/{self.publish}")
	
	def get_absolute_url(self):
		return(reverse("books:book_detail",args=[self.slug]))