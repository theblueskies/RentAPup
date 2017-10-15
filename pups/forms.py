from datetime import date, datetime
from calendar import monthrange

from django import forms

from pups import stripe_settings


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ProfileForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=100)
    lastname = forms.CharField(label='Last Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    email = forms.EmailField()
    renter = forms.BooleanField(required=False)
    name_of_dog = forms.CharField(label='Name of dog', max_length=100, required=False)
    breed_of_dog = forms.CharField(label='Breed of dog', max_length=100, required=False)
    age_of_dog = forms.IntegerField(required=False)


class PuppyForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=100)
    age = forms.IntegerField()
    breed = forms.CharField(label='Breed', max_length=100)

def PaymentForm(request):
    context = { "stripe_key": stripe_settings.STRIPE_PUBLIC_KEY }
    return render(request, "checkout.html", context)
