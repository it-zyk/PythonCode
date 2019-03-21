

from django.conf.urls import include, url
from user import views

urlpatterns = [
    url(r'^register$', views.register, name='register'),  # 注册
    url(r'^register_handle$', views.register, name='register_handle'),  # 注册处理
index
]
