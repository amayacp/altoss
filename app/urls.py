from django.urls import path
from.import views

urlpatterns = [

  
    path('',views.home,name='home'),
    path('training',views.training,name='training'),
    path('contact',views.contact,name='contact'),
     path('course',views.course,name='course'),
      path('base',views.base,name='base'),
    path('add_user',views.add_user,name='add_user'),
     path('reg',views.reg,name='reg'),
      path('enquerys',views.enquerys,name='enquerys'),
      path('app',views.app,name='app'),
      path('ex',views.ex,name='ex'),
    
]