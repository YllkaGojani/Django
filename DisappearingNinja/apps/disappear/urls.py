from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas/(?P<color>[a-z]*)$',views.ninjas)
]
