from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^3dscatters$', views.show3DScatters, name='3dscatters'),
    url(r'^ajaxtest', views.showAjaxhtml, name='ajaxtest'),
    url(r'^ajax-list$', views.ajax_list, name='ajax-list'),
    url(r'^ajax-dict$', views.ajax_dict, name='ajax-dict'),
    url(r'^location$', views.getLocation, name='location'),
    url(r'^location2$', views.getLocation2, name='location2'),
    url(r'^getrandom$', views.generateRandom, name='getrandom')
]
