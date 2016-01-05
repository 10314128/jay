from django.conf.urls import url
from album import views

urlpatterns = [
    url(r'^$', views.album, name='album'),
    
]