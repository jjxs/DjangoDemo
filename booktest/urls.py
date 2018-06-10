from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('getTest1/', views.getTest1),
    path('getTest2/', views.getTest2),
    path('getTest3/', views.getTest3),
    path('postTest1/', views.postTest1),
    path('postTest2/', views.postTest2),
    path('redTest/', views.redTest),
    url(r'^returnTest/(\d+)$',views.returnTest, name='show'),

]
