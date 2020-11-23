from django.urls import path 
from .views import author_detail_view

app_name="author"

urlpatterns = [
	path("author/<slug:slug>/",author_detail_view.as_view(),name="author_detail")
]