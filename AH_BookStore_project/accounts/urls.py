from django.urls import path,include
from .views import user_login_view,user_profile_view

app_name="accounts"

urlpatterns = [
	path("profile/",user_profile_view,name="profile"),
	path("login/",user_login_view,name="login"),
	path("",include("django.contrib.auth.urls")),
]