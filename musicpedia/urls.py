from django.contrib import admin
from django.urls import include,path
from music import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
]
