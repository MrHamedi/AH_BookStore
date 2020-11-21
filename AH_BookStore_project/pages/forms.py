from django import forms 
 

class ContactUsForm(forms.Form):
	advice=forms.CharField(widget=forms.Textarea)
	