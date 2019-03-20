

from django.conf.urls import include, url
from user import views

urlpatterns = [
    url(r'^register$', include(admin.site.urls), name='register'), #注册
]
