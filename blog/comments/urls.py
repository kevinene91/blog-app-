from django.conf.urls import  url

from .views import (
	comment_thread,
	comment_delete 
	
	)

urlpatterns =[
 
   
    url(r'^(?P<id>[\w-]+)/$', comment_thread,  name='thread'),
	url(r'^(?P<id>[\w-]+)/delete/$', comment_delete, name='delete'),

]