from django.db import models 
from django.conf import settings 
from django.contrib.auth.models import User 

class Profile(models.Model):
	image=models.ImageField(upload_to="profile/Y/m/d/",null=True,blank=True)
	email_confirmed=models.BooleanField(blank=True)
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
	code=models.BigIntegerField()
	def __str__(self):
		return(self.user.username)