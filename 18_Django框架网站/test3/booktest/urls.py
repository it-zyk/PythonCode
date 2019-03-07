
from django.conf.urls import include, url
from django.contrib import admin
from booktest import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', views.index),
    # 捕获位置参数
    # url(r'^showarg(\d+)$', views.show_arg)
    # 捕获关键字参数
    url(r'^showarg(?P<num>\d+)$', views.show_arg),
]
