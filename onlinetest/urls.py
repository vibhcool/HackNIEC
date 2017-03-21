from django.conf.urls import url

from . import views


app_name = 'onlinetest' 
#This sets application namespace to diffretiate urls of different apps.

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),
    #url for login-page:
    url(r'^studentlogin$', views.studentlogin, name='studentlogin'),
    url(r'^clientlogin$', views.clientlogin, name='clientlogin'),
    #url for signup-page:
    url(r'^clientregister$', views.clientregister, name='clientregister'),
    url(r'^clientadmin$', views.clientadmin, name='clientadmin'),
    url(r'^clientloginval$', views.clientloginval, name='clientloginval'),
    url(r'^studentloginval$', views.studentloginval, name='studentloginval'),
    url(r'^studenthome$', views.studenthome, name='studenthome'),
    url(r'^yourtest$', views.yourtest, name='yourtest'),
    url(r'^studentInfo', views.studentInfo, name='studentInfo'),
    url(r'^clientlogout$', views.clientlogout, name='clientlogout'),


    #url to log in a user:
   # url(r'^log_req$', views.logInReq, name='login_req'),

    #url for create-user:
    #url(r'^register_user$', views.register, name='register_user'),
    #url(r'^register$',views.register, name='register')
    
]
