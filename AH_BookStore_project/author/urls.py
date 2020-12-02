from django.urls import path 
from .views import author_detail_view

app_name="author"

urlpatterns = [
	path("detail/<int:id>/",author_detail_view,name="author_detail")
]