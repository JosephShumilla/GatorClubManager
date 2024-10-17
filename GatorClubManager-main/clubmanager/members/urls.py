from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name="login"),
    path('signUp', views.signup_user, name='signup')
]