from django.conf.urls import url

from . import views
from . import payment_views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^charge/$', payment_views.charge, name="charge"),
    url(r'^user-profile$', views.user_profile, name='index'),
]
