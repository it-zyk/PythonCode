
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', views.index),
]
