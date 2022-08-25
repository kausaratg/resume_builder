from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.Home.as_view(), name="index"),
    path('home/', views.signup_user, name="signup"),
    path('signin/', views.signin_user, name="signin")
]
