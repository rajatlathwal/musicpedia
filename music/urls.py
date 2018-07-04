from django.urls import path
from django.conf.urls import url
from . import views

app_name="music"

urlpatterns = [
    path('', views.index , name='index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite , name='favourite'),
    url(r'^register/$',views.UserFormView.as_view(), name='register')


]

