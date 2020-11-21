from django import forms
from django.contrib.auth.models import User 
from .models import Profile

class UserLoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={"class":"LoginPageField"}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"LoginPageField"}))
	

class UserRegisterForm(forms.ModelForm):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput(),label="password")
	password2=forms.CharField(widget=forms.PasswordInput(),label="repeat password")
	class Meta:
		model=User 
		fields=("first_name","last_name","email")

	def clean_password2(self):
		password=self.cleaned_data["password"]
		password2=self.cleaned_data["password2"]
		if(len(password2)>=8):
			if(password==password2):
				return(password)
			else:
				raise(forms.ValidationError("The passwords are not matched"))
		else:
			raise(forms.ValidationError("The password must be longer than 8"))


class ProfileUpdateForm(forms.ModelForm):
	
	class Meta:
		model=Profile
		fields=("image",)
