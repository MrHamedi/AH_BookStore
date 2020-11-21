from django.urls import path,include
from .views import user_login_view,user_profile_view,user_register_view,profile_update_view,email_activate_view


app_name="accounts"

urlpatterns = [
	path("user_register/",user_register_view,name="user_register"),
	path("profile/",user_profile_view,name="profile"),
	path("login/",user_login_view,name="login"),
	path("",include("django.contrib.auth.urls")),
	path("image_update/",profile_update_view,name="profile_update"),
	path("email_activate/<int:code>/",email_activate_view,name="email_activate"),
]