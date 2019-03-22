

from django.conf.urls import include, url
from user import views
from user.views import RegisterView, LoginView, ActiveView, LogoutView, UserInfoView, UserOrderView, AddressView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # url(r'^register$', views.register, name='register'),  # 注册
    # url(r'^register_handle$', views.register_handle, name='register_handle'),  # 注册处理
    url(r'^register$', RegisterView.as_view(), name='register'),  # 用户注册
    url(r'^login$', LoginView.as_view(), name='login'),  # 登录
    url(r'^logout$', LogoutView.as_view(), name='logout'),  # 注销登录
    url(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),  # 用户激活

    url(r'^$', login_required(UserInfoView.as_view()), name='user'),  # 用户中心-信息页

    # url(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心-首页
    url(r'^order$', UserOrderView.as_view(), name='order'),  # 用户首页-订单
    url(r'^address$', AddressView.as_view(), name='address'),  # 用户中心地址

]
