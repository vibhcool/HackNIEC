from django.conf.urls import url

from . import views


app_name = 'onlinetest' 
#This sets application namespace to diffretiate urls of different apps.

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),
    #url for login-page:
    url(r'^login$', views.login, name='login'),
    #url for signup-page:
    url(r'^signup$', views.signup, name='signup'),

    #url to log in a user:
    url(r'^log_req$', views.logInReq, name='login_req'),

    #url for create-user:
    url(r'^register_user$', views.register, name='register_user'),
    
]
