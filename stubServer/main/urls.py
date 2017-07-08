from django.conf.urls import url

from . import views


urlpatterns = [
		url(r'^files/(?P<filename>.+)$',views.files, name = 'files'),
		url(r'^testpost$', views.testpost, name = 'testpost'),
		url(r'^testget$', views.testget, name = 'testget'),
		url(r'^$', views.index, name = 'index')
]
