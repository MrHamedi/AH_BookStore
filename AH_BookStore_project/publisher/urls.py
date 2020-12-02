from django.urls import path 
from .views import publisher_detail_view

app_name="publisher"

urlpatterns = [
	path("detail/<int:id>/",publisher_detail_view,name="publisher_detail"),
]