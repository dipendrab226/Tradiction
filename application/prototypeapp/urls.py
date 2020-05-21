from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    url('^registration$', views.registration, name='registration'),
    url(r'^expertregistration$', views.expertregistration, name='expertregistration'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^forgotpwd$', views.forgotpwd, name='forgotpwd'),
    url(r'^getpwd$', views.getpwd, name='getpwd'),
    url(r'^addtrader$', views.addtrader, name='addtrader'),
    url(r'^addexpert$', views.addexpert, name='addexpert'),
    url(r'^logindata$', views.logindata, name='logindata'),
    url(r'^verifyexpert$', views.verifyexpert,name='verifyexpert'),
    url(r'^verifytrader$', views.verifytrader,name='verifytrader'),
    url(r'^acceptexpert$', views.acceptexpert,name='acceptexpert'),
    url(r'^rejectexpert$', views.rejectexpert,name='rejectexpert'),
    url(r'^rejecttrader$', views.rejecttrader,name='rejecttrader'),
    url(r'^accepttrader$', views.accepttrader,name='accepttrader'),
    url(r'^index$', views.index, name='index'),
    url(r'^stocks$', views.stocks, name='stocks'),
    url(r'^news$', views.news, name='news'),
    url(r'^watchlist$', views.watchlist, name='watchlist'),
    url(r'^help$', views.help, name='help'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^tradinghistory$', views.tradinghistory, name='tradinghistory'),
   # url(r'^search$', views.search, name='search'),
    url(r'^stockdetails$', views.stockdetails, name='stockdetails'),
    url(r'^addtowatchlist', views.addtowatchlist, name='addtowatchlist'),
    url(r'^removefromwatchlist', views.removefromwatchlist, name='removefromwatchlist'),
    url(r'^addstocks$', views.addstocks, name='addstocks'),
    url(r'^buystocks$', views.buystocks, name='buystocks'),
    url(r'^sellstocks$', views.sellstocks, name='sellstocks'),
    url(r'^sells$', views.sells, name='sells'),
    url(r'^between', views.between, name='between'),
    url(r'^home', views.Home, name='home'),
    url(r'^success', views.success, name='success'),
    url(r'^failure', views.failure, name='failure'),
    url(r'^myprofile', views.myprofile, name='myprofile'),
    url(r'^updateinfo', views.updateinfo, name='updateinfo'),
    url(r'^updatebankinfo', views.updatebankinfo, name='updatebankinfo'),
    url(r'^updatepwd', views.updatepwd, name='updatepwd'),

]