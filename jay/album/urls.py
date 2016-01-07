from django.conf.urls import url
from album import views

urlpatterns = [
    url(r'^$', views.album, name='album'),
    url(r'^category/(?P<categoryName>[\w\-]+)/$', views.category, name='category'),
    url(r'^addCategory/$', views.addCategory, name='addCategory'),
    url(r'^addPage/(?P<categoryName>[\w\-]+)/$', views.addPage, name='addPage'),
    url(r'^deleteCategory/(?P<categoryID>[0-9]+)/$', views.deleteCategory,name='deleteCategory'),
]