from django.conf.urls import url

from . import views

app_name = 'cronos'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.profile, name='profile'),
]
