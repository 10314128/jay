from django.conf.urls import url
from pic import views

urlpatterns = [
    url(r'^$', views.pic, name='pic'),
]