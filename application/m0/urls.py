from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="m0-home"),
    path('about-brian/', views.about_brian, name="about_brian"),
    path('about-ben/', views.about_ben, name="about_ben"),
    path('about-may/', views.about_may, name="about_may"),
    path('about-kevin/', views.about_kevin, name="about_kevin"),
    path('about-sanjay/', views.about_sanjay, name="about_sanjay"),
    path('about-dibs/', views.about_dibs, name="about_dibs"),

]