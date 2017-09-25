from django.conf.urls import url
from . import views    

urlpatterns = [
	url(r'^$', views.index),
	url(r'^index$', views.index),
	url(r'^semirestusers/index$', views.index),
	url(r'^new$', views.new),
	url(r'^create$', views.create),
	url(r'^show/(?P<user_id>\d+)/$', views.show),
	url(r'^update/(?P<user_id>\d+)/$', views.update),
	url(r'^destroy/(?P<user_id>\d+)$', views.destroy)
]	