from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home, name='Home'),

    path('view/', views.view,name="view Customer's detail"),
    path('Register/' ,views.Register , name='Register'),
    path('transfer/<str:username>', views.transfer, name='transfer'),

]
#'transfer/<str:username>'
