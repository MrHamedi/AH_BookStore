from django.db import models
from datetime import datetime

# Create your models here.
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
