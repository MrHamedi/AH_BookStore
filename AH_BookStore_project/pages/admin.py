from django.contrib import admin
from .models import Page 

class PagesAdmin(admin.ModelAdmin):
	list_display=("title","permalink","create","update")
	list_filter=("title","create")
	search_fields=("title","permalink")
	def __str__(self):
		return(self.create)

admin.site.register(Page,PagesAdmin)
