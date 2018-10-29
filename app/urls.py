from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^entry/$', views.entry, name='entry'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^check_phone/$', views.check_phone, name='check_phone'),
]