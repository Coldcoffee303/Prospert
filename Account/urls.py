from django.urls import path
from . import views


urlpatterns = [
	path('signup/',views.SignUpPage,name='SignUp'),
	path('login/',views.loginPage,name='Login'),
	path('logout/',views.logoutPage,name='Logout'),
]