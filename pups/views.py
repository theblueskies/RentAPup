import json

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from pups.models import Puppy
from pups.models import UserProfile as Profile
from pups.forms import ProfileForm, PuppyForm


def index(request):
    puppies = Puppy.objects.all() # Gets all puppy instances from DB
    template = loader.get_template('pups/home.html') # Selects template to use
    if request.user:
        context = {
            'puppies': 'user is authenticated'
        }
    else:
        print ("Not authenticated")
        return redirect('login')

    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'pups/signup.html', {'form': form})


def user_profile(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print (form.cleaned_data)
            user = request.user
            user.firstname = form.cleaned_data['firstname']
            user.lastname = form.cleaned_data['lastname']
            user.address = form.cleaned_data['address']
            user.email = form.cleaned_data['email']
            user.save()

            profile = Profile(active_user=user,
                              renter=form.cleaned_data['renter'])
            profile.save()

            puppy = Puppy(owner=request.user,
                          name=form.cleaned_data['name_of_dog'],
                          breed=form.cleaned_data['breed_of_dog'],
                          age=form.cleaned_data['age_of_dog'])
            puppy.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('/app/puppy/')

    # if a GET (or any other method) we'll create a blank form
    else:
        if request.user:
            profile = Profile.objects.filter(active_user=request.user)
            if not profile.exists():
                form = ProfileForm()
                return render(request, 'pups/profile_create.html', {'form': form})
            else:
                url = reverse('home')
                return redirect(url)


def home(request):
    if request.method == 'GET':
        if request.user:
            profile = Profile.objects.filter(active_user=request.user).first()
            if getattr(profile, 'renter', None) == None:
                return redirect(reverse('user_profile'))
            else:
                return redirect(reverse('get_or_rent_puppy'))


def get_or_rent_puppy(request):
    if request.method == 'GET':
        context = {}
        profile = Profile.objects.filter(active_user=request.user).first()
        if profile.renter == True:
            template = loader.get_template('pups/renter.html')
        else:
            template = loader.get_template('pups/owner.html')
        return HttpResponse(template.render(context, request))
