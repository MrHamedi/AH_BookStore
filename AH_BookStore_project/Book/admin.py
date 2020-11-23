from django.contrib import admin 
from .models import Book

class BookAdmin(admin.ModelAdmin):
	list_display=("name","authors_list","publish","offer_time")
	prepopulated_fields={"slug":("author","name","publish")}


admin.site.register(Book,BookAdmin)
