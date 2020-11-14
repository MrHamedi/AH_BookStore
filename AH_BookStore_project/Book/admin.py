from django.contrib import admin 
from .models import Author,Publisher,Book

class BookAdmin(admin.ModelAdmin):
	list_display=("name","authors_list","publish","offer_time")
	prepopulated_fields={"slug":("author","name","publish")}

class AuthorAdmin(admin.ModelAdmin):
	list_display=("name",)
	prepopulated_fields={"slug":("name","birthday")}


class PublisherAdmin(admin.ModelAdmin):
	list_display=("name",)
	prepopulated_fields={"slug":("name",)}


admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher,PublisherAdmin)