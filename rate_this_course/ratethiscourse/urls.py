from django.conf.urls import patterns, url
from ratethiscourse import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/?$', views.register, name='register'),
    url(r'^login/?$', views.user_login, name='login'),
    url(r'^logout/?$', views.user_logout, name='logout'),
    url(r'^add_course/?$', views.add_course, name='add course'),
    url(r'^university/(?P<uni_name_url>\w+)/?$', views.university, name='university'),
    url(r'^university/(?P<uni_name_url>\w+)/(?P<course_name_url>\w+)/?$', views.course, name='course'),
    url(r'^university/(?P<uni_name_url>\w+)/(?P<course_name_url>\w+)/(?P<module_name_url>\w+)/?$', views.module, name='module'),
    )
