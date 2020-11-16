from django import forms 


class UserLoginForm(forms.Form):
	username=forms.CharField(widget=forms.TextInput(attrs={"class":"LoginPageField"}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"LoginPageField"}))
	