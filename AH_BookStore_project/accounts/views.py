from django.shortcuts import render 
from django.contrib.auth import authenticate,login 
from django.contrib import messages 
from django.http import HttpResponseRedirect
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse 


def user_login_view(request):
	if(request.method=="POST"):
		form=UserLoginForm(data=request.POST)
		if(form.is_valid()):
			cd=form.cleaned_data 
			user=authenticate(request,username=cd["username"],password=cd["password"])
			if(user is not None):
				if(user.is_active):
					login(request,user)
					return(HttpResponseRedirect(reverse("accounts:profile")))
				else:
					messages.error(request,"The account have been blocked for some reasons")
			else:
				messages.error(request,"The username or password is incorrect")
	else:
		form=UserLoginForm()
	return(render(request,"accounts/login.html",{"form":form}))


@login_required(login_url="/accounts/login")
def user_profile_view(request):
	user=request.user
	context={
	"name":user.first_name,
	"family":user.last_name,
	"username":user.username,
	"email":user.email
	}
	return(render(request,"accounts/profile.html",context))