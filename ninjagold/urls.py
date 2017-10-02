from django.conf.urls import url
from . import views    

urlpatterns = [
	url(r'^$', views.index),
	url(r'^Amadon/index$', views.index),
	url(r'^Amadon/buy$', views.buy),
	url(r'^Amadon/checkout$', views.buy),	
	url(r'^Amadon/clear$', views.clear)
  ]
  