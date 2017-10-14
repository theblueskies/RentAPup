import json

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

from pups.models import Puppy
from pups.forms import ProfileForm, PuppyForm


def index(request):
    puppies = Puppy.objects.all() # Gets all puppy instances from DB
    template = loader.get_template('pups/home.html') # Selects template to use
    context = {
        'puppies': puppies
    }
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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfileForm()

    return render(request, 'pups/profile_create.html', {'form': form})
