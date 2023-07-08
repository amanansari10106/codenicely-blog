from django.urls import path
from usersapp import apis

urlpatterns = [
    path("register/", apis.RegisterAPI.as_view(), name="registerAPI"),
    path("login/", apis.LoginAPI.as_view(), name="loginAPI"),
    path("details/", apis.GetUserDetailsAPI.as_view(),name="getUserDetailsAPI"),
]