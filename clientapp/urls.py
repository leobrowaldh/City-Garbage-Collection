from django.urls import include,path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('request',views.request_view,name='request'),
    path('post_request',views.post_request,name='post_request'),
    path('requests',views.requests_view,name='requests'),
    path('login',auth_views.login,{'template_name':'clientapp/login.html'},name='login'),
    path('logout',auth_views.logout,{'next_page':'/'},name='logout')
]
