from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.Home.as_view(), name="index"),
    path('signup/', views.signup_user, name="signup"),
    path('signin/', views.signin_user, name="signin"),
    path('logout', views.logout_user, name="logout"),
    path('personal_info/', views.personal_info.as_view(), name="personal_info"),
    path('update_info<str:pk>', views.UpdatePersonal_info.as_view(), name="update_info")
]
