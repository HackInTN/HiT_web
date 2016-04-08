"""hackintn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin/', admin.site.urls),
    #url(r'^validate_account', views.user_validate),
    url(r'^reqLogin', views.reqLogin),
    url(r'^login', views.user_login),
    url(r'logout', views.user_logout),
    url(r'^register', views.user_register),

    url(r'^users$', views.get_users),
    url(r'^users/(?P<Id>[0-9]+)$', views.get_user),

    url(r'^challenges$', views.get_challenges),
    url(r'^challenges/(?P<Id>[0-9]+)$', views.get_challenge),
    url(r'^challenges/(?P<Id>[0-9]+)/start$', views.start_challenge),
    url(r'^challenges/(?P<Id>[0-9]+)/stop$', views.stop_challenge),
    url(r'^challenges/(?P<Id>[0-9]+)/validate$', views.validate_challenge),
    url(r'^ex/(?P<path>.*)$', views.DockerMultiplexView.as_view())
]
