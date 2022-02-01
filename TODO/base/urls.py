import imp
from django.urls import path
from .views import Login, TaskList , TaskCreate
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',Login.as_view(),name='login'), # to go to the login page 
    path('logout/',LogoutView.as_view(next_page = 'login'),name='logout'), # if the user logouts , they should be redirected to the login page again
    path('',TaskList.as_view(),name='tasklist'),
    path('create/',TaskCreate.as_view(),name='taskcreate')

]
