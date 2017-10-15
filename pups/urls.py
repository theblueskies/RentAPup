from django.conf.urls import url

from . import views
from . import payment_views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r"^checkout$", payment_views.checkout, name="checkout"),
    url(r"^payment_form$", payment_views.payment_form, name="payment_form"),
    url(r'^user-profile/$', views.user_profile, name='user_profile'),
    url(r'^edit-profile/$', views.edit_profile, name='edit_profile'),
    url(r'^home/$', views.home, name='home'),
    url(r'^puppy/$', views.get_or_rent_puppy, name='get_or_rent_puppy'),
]
