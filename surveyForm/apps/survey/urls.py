from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^survey/process$', views.process),
    url(r'^result$', views.result)
]