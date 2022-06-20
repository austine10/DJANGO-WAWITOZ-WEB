from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('more', views.more, name='more'),
    path('home', views.back_home, name='back'),
    path('moreI', views.more_i, name='more_i'),
    path('career',views.career,name='career'),
    path('jobs', views.jobs, name='jobs'),
    path('apply', views.apply, name='apply'),
    path('apply/', views.apply_btn, name='apply_btn'),

path('moreB', views.more_b, name='more_b'),
]
