from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.Home.as_view(), name="index"),
    path('signup/', views.signup_user, name="signup"),
    path('signin/', views.signin_user, name="signin"),
    path('logout', views.logout_user, name="logout"),
    path('personal_info/', views.personal_info.as_view(), name="personal_info"),
    path('update_info/<str:pk>', views.UpdatePersonal_info.as_view(), name="update_info"),
    path('cv_template', views.cv_list.as_view(), name="cv_template"),
    path('text/', views.test_template.as_view(), name="text"),
    path('template2/', views.text_template2.as_view(), name="template2"),
    path('template3/', views.text_template3.as_view(), name="template3"),
    path('template4/', views.text_template4.as_view(), name="template4"),
    path('template5/', views.text_template5.as_view(), name="template5"),
]
