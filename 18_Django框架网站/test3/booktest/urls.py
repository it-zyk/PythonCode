
from django.conf.urls import include, url
from django.contrib import admin
from booktest import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', views.index),
    # 捕获位置参数
    # url(r'^showarg(\d+)$', views.show_arg)
    # 捕获关键字参数http://localhost:8000/showarg22
    url(r'^showarg(?P<num>\d+)$', views.show_arg),
    url(r'^showarg(?P<num>\d+)$', views.show_arg),
    # 显示登录页面
    url(r'^login$', views.login),
    # 用户校验
    url(r'^login_check$', views.login_check),
    url(r'^test_ajax$', views.ajax_test)
    url(r'^ajax_handle$', views.ajax_handle)
    url(r'^set_cookie$', views.set_cookie)  # 设置cookies
    url(r'^get_cookie$', views.get_cookie)  # 获取cookies

    url(r'^set_session$', views.set_session),  # 设置session
    url(r'^get_session$', views.get_session),  # 获取session
    url(r'^clear_session$', views.clear_session),  # 清除session
]
