from django.shortcuts import render 
from .models import Page 
from django.core.mail import send_mail,get_connection
from django.http import HttpResponse
from .forms import ContactUsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def index_page_view(request,permalink):
	#achives the page by its permalink attribute
	page=Page.objects.get(permalink="/"+permalink)
	return(render(request,"pages/index.html",{"title":page.title,"content":page.content,}))

@login_required(login_url="/accounts/login")
def contact_us_view(request):
	if(request.method=="POST"):
		form=ContactUsForm(data=request.POST)
		user=request.user
		if(form.is_valid()):
			cd=form.cleaned_data 
			subject=f"This is a advice from {user.first_name} {user.last_name} with username : {user.username}."
			content=cd["advice"]
			send_mail(subject,content,user.username,["ahmadihamed167@gmail.com"],fail_silently=False)
			messages.success(request,"Thanks,The messages sent successfuly")
	else:
		form=ContactUsForm()
	return(render(request,"pages/contact_us.html",{"form":form}))