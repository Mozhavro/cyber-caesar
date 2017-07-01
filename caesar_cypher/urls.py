from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^encrypt/', views.encrypt),
    url(r'^decrypt/', views.decrypt),
]