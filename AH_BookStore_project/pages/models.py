from django.db import models 
from django.utils import timezone 

class Page(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField("The content of the page")
	permalink=models.CharField(max_length=50,unique=True)
	create=models.DateField(auto_now_add=True)
	update=models.DateField(auto_now=True,blank=True,null=True)
	class Meta:
		ordering=("-create",)

	def __str__(self):
		return(self.title)