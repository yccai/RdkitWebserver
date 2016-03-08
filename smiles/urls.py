from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/validate/
    url(r'^([^J][A-Za-z0-9@+\-\[\]\(\)\\=#$]+)/validate$', views.validate, name='validate'),
    url(r'^([^J][A-Za-z0-9@+\-\[\]\(\)\\=#$]+)/png$', views.png, name='png'),
    url(r'^([^J][A-Za-z0-9@+\-\[\]\(\)\\=#$]+)/svg$', views.svg, name='svg'),
]
