from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="comment"),
    url(r'^test/$', views.test, name="test")
]