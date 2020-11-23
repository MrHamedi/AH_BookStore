from django.contrib import admin
from .models import Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display=("name",)
	prepopulated_fields={"slug":("name","birthday")}



admin.site.register(Author,AuthorAdmin)
