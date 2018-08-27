from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
	path('', views.index, name='index'),
	url(r'^permission-denied/$', views.perm_denied, name='perm-denied'),
	url(r'^ps/$', views.PostListView.as_view(), name='posts'),
	url(r'^p/(?P<pk>[-\w]+)$', views.PostDetailView.as_view(), name='post-detail'),
]

urlpatterns += [  
    url(r'^p/add/$', views.PostCreate.as_view(), name='post_create'),
    url(r'^p/(?P<pk>[-\w]+)/update/$', views.user_permitted(views.PostUpdate.as_view()), name='post_update'),
    url(r'^p/(?P<pk>[-\w]+)/delete/$', views.user_permitted(views.PostDelete.as_view()), name='post_delete'),
    url(r'^t/(?P<tag>[-\w]+)/$', views.search_by_tag, name='tag_search'),
    url(r'^search/$', views.search, name='tag_search_form'),
   ]