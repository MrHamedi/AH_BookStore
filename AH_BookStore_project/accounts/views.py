from django.shortcuts import render 
from django.contrib.auth import authenticate,login 
from django.contrib import messages 
from django.http import HttpResponseRedirect
from .forms import UserLoginForm,UserRegisterForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse 
from django.contrib.auth.models import User
from random import randrange
from .models import Profile
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail


def user_login_view(request):
	if(request.method=="POST"):
		form=UserLoginForm(data=request.POST)
		if(form.is_valid()):
			cd=form.cleaned_data 
			user=authenticate(request,username=cd["username"],password=cd["password"])
			if(user is not None):
				if(user.is_active):
					login(request,user)
					return(HttpResponseRedirect("/"))
				else:
					messages.error(request,"Your account is not active please go to email adress we have sent an email containing the adress to active it.")
			else:
				messages.error(request,"The username or password is incorrect \n Did you activate your account.\n we sent an email to your email adress with path to activate your account.")
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
	"email":user.email,
	}
	return(render(request,"accounts/profile.html",context))


def user_register_view(request):
	if(request.method=="POST"):
		form=UserRegisterForm(data=request.POST)
		if(form.is_valid()):
			cd=form.cleaned_data
			new_user=form.save(commit=False)
			new_user.username=cd["username"]
			new_user.set_password(cd["password"])
			new_user.is_active=False
			code=randrange(100000,1000000)
			#This messages containce the adress to activate account that sends to user email
			subject="actuator account adress for AH_BookStore."
			message=f"Hi,we have recived a request to active a account on your email.\n please get into this adress to activate 127.0.0.1:8000/accounts/email_activate/{code}/ \n If it was not you please ignore this message."
			profile=Profile(user=new_user,email_confirmed=False,code=code)
			send_mail(subject,message,"AH Book Store",[cd["email"],],fail_silently=False)
			new_user.save()
			profile.save()
			return(HttpResponseRedirect(reverse("accounts:login")))

	else:
		form=UserRegisterForm()
	return(render(request,"accounts/user_register.html",{"form":form}))


def profile_update_view(request):
	if(request.method=="POST"):
		form=ProfileUpdateForm(files=request.FILES,instance=request.user.profile)
		if(form.is_valid()):
			form.save()			
	else:
		form=ProfileUpdateForm(instance=request.user.profile)
	return(render(request,"accounts/profile_update.html",{"form":form}))

def email_activate_view(request,code):
	profile=get_object_or_404(Profile,code=code)
	user=User.objects.get(profile=profile)
	user.is_active=True
	user.save()
	messages.success(request,"The email activated successfuly")
	return(render(request,"accounts/email_activated.html",{}))


