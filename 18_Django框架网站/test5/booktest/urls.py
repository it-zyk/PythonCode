from django.conf.urls import include, url
from django.contrib import admin
# from booktest import views
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^static_test$', views.static_test),

]
