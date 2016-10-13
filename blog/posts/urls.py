from django.conf.urls import  url

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	about_me, 
	)

urlpatterns =[
 
    url(r'^$',post_list, name='list'),
    url(r'^about_me/$',about_me, name='about_me'),

	url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w.@+-]+)/$', post_detail,  name='detail'),
    url(r'^(?P<slug>[\w.@+-]+)/edit/$', post_update, name='update'),
	url(r'^(?P<slug>[\w.@+-]+)/delete/$', post_delete),


]