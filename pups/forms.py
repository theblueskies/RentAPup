from django import forms


class ProfileForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=100)
    lastname = forms.CharField(label='Last Name', max_length=100)
    address = forms.CharField(label='Address', max_length=100)
    email = forms.EmailField()
    renter = forms.BooleanField()


class PuppyForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=100)
    age = forms.IntegerField()
    breed = forms.CharField(label='Breed', max_length=100)
