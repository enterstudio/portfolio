from django.conf.urls import patterns, url

from projects import views

urlpatterns = patterns('',
    #loads home page
    url(r'^$', views.index, name='index'),
    #loads portfolio page listing
    url(r'^portfolio/?$', views.projects, name='projects'),
    #loads single project detail page
    url(r'^portfolio/(?P<project_id>\d+)/?$', views.project_detail, name='project_detail'),
    #load blog page (lists posts)
    url(r'^posts/?$', views.posts, name='posts'),
    #loads single post detail page
    url(r'^posts/(?P<post_id>\d+)/?$', views.post_detail, name='post_detail'),
    #loads resume page
    url(r'^resume/?$', views.resume, name='resume'),
    
    
)

