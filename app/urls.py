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

    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('admin',views.admin,name='admin'),
    path('user_login',views.user_login,name='user_login'),
    path('base2',views.base2,name='base2'),
    
    path('edit_user/<int:pk>',views.edit_user,name="edit_user"),
    path('delete_user/<int:pk>',views.delete_user,name="delete_user"),
    path('msg',views.msg,name='msg'),
    path('regist',views.regist,name='regist'),
    path('delete_reg/<int:pk>',views.delete_reg,name="delete_reg"),
    path('enquir',views.enquir,name='enquir'),
    path('delete_enq/<int:pk>',views.delete_enq,name="delete_enq"),
     path('appl',views.appl,name='appl'),
    path('delete_apply/<int:pk>',views.delete_apply,name="delete_apply"),

]