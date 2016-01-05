from django.conf.urls import url
from video import views

urlpatterns = [
    url(r'^$', views.video, name='video'),
]