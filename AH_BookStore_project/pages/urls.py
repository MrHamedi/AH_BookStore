from django.urls import path 
from .views import index_page_view

app_name="pages"

urlpatterns=[	
	path("<str:permalink>/",index_page_view,name="index"),
]