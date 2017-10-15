from django.conf.urls import url

from . import views
from . import payment_views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^user-profile$', views.user_profile, name='index'),
    url(r"^checkout$", payment_views.checkout, name="checkout"),
    url(r"^payment_form$", payment_views.payment_form, name="payment_form")
]
