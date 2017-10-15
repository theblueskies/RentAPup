from django.conf.urls import url

from . import views
from . import payment_views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^charge/$', payment_views.charge, name="charge"),
    url(r'^user-profile/$', views.user_profile, name='user_profile'),
    url(r'^home/$', views.home, name='home'),
    url(r'^puppy/$', views.get_or_rent_puppy, name='get_or_rent_puppy'),
]
