from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^home$', views.home, name='home'),
    url(r'^login$', views.login, name='login'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^regdata$', views.regdata, name='regdata'),
    url(r'^logindata$', views.logindata, name='logindata'),
    url(r'^viewindex$', views.viewindex, name='viewindex'),
    url(r'^search$', views.search, name='search'),

]