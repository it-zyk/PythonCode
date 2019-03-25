from django.conf.urls import include, url
from goods import views

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 首页
]
