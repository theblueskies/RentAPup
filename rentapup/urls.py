"""rentapup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.static import serve

from pups import views
admin.site.site_header = 'Puppy Playdates Administration'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^app/', include('pups.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'pups/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'pups/logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
