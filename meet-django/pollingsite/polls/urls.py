from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
	url(r'^meet/$,views.hello, name="pizza")