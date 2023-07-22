from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.index,name='Twitter-clone'),
    path("create_post",views.create_post,name='twitter_home')
]
