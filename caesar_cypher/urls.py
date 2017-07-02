from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^encrypt/', views.encrypt, name="encrypt"),
    url(r'^decrypt/', views.decrypt, name="decrypt"),
    url(r'^break-cipher/', views.break_cipher, name="break"),
]