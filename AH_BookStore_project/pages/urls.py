from django.urls import path 
from .views import index_page_view,contact_us_view

app_name="pages"

urlpatterns = [	
	path("contact_us/",contact_us_view,name="contact_us"),
	path("<str:permalink>/",index_page_view,name="index"),
]