from django.conf.urls import patterns, url
from ratethiscourse import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/?$', views.register, name='register'),
    url(r'^login/?$', views.user_login, name='login'),
    url(r'^logout/?$', views.user_logout, name='logout'),
    url(r'^add_course/?$', views.add_course, name='add course'),
    url(r'^add_module/?$', views.add_module, name='add module'),
    url(r'^user_profile/?$', views.user_profile, name='user profile'),
    url(r'^validate_user/?$', views.validate_user, name='validate user'),
    url(r'^resend_validation_email/?$', views.resend_validation_email, name='resend validation email'),
    url(r'^university/?$', views.universities, name='universities'), 
    url(r'^university/(?P<uni_name_url>\w+)/?$', views.university, name='university'),
    url(r'^university/(?P<uni_name_url>\w+)/(?P<course_name_url>\w+)/?$', views.course, name='course'),
    url(r'^university/(?P<uni_name_url>\w+)/(?P<course_name_url>\w+)/(?P<module_name_url>\w+)/?$', views.module, name='module'),
    url(r'^get_courses/?$', views.get_courses, name='get courses'),
    url(r'^get_user_uni/?$', views.get_user_uni, name='get user uni'),
    url(r'^get_user_course/?$', views.get_user_course, name='get user course'),
    url(r'^ajax_login/?$', views.ajax_login, name='ajax login'),
    url(r'^ajax_logout/?$', views.ajax_logout, name='ajax logout'),
    )
