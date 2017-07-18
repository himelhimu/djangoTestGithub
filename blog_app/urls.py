from django.conf.urls import url

from blog_app import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^post/new/$',views.post_new,name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]