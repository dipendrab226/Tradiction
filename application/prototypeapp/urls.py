from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^registration$', views.registration, name='registration'),
    url(r'^expertregistration$', views.expertregistration, name='expertregistration'),
    url(r'^login$', views.login, name='login'),
    url(r'^addtrader$', views.addtrader, name='addtrader'),
    url(r'^addexpert$', views.addexpert, name='addexpert'),
    url(r'^logindata$', views.logindata, name='logindata'),
    url(r'^index$', views.index, name='index'),
    url(r'^stocks', views.stocks, name='stocks'),
    url(r'^news', views.news, name='news'),
    url(r'^watchlist', views.watchlist, name='watchlist'),
    url(r'^help', views.help, name='help'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
    url(r'^tradinghistory', views.tradinghistory, name='tradinghistory'),
    url(r'^search', views.search, name='search')
]