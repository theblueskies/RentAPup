from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    url(r'^user-profile$', views.user_profile, name='index'),
]
