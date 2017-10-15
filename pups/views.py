import json

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
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
    template = loader.get_template('pups/base.html') # Selects template to use
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
            return redirect('login')
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
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.save()

            profile = Profile(active_user=user,
                              renter=form.cleaned_data['renter'],
                              address=form.cleaned_data['address'])
            profile.save()

            try:
                if form.cleaned_data['renter'] == False:
                    puppy = Puppy(owner=request.user,
                                  name=form.cleaned_data['name_of_dog'],
                                  breed=form.cleaned_data['breed_of_dog'],
                                  age=form.cleaned_data['age_of_dog'])
                    puppy.save()
            except:
                # DB error will be thrown if puppy fails to save. At that time
                # we want to clear the profile created too.
                profile.delete()
                return redirect('/app/user-profile/')
            else:
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
        if profile and profile.renter == True:
            available_puppies = Puppy.objects.filter(rented_now=False).first()
            if available_puppies:
                context['are_puppies_available'] = True
            template = loader.get_template('pups/renter.html')
        else:
            template = loader.get_template('pups/owner.html')
        return HttpResponse(template.render(context, request))


def edit_profile(request):
    profile = get_object_or_404(Profile, active_user=request.user)
    puppy = Puppy.objects.filter(owner=request.user).first()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print (form.cleaned_data)
            user = request.user
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.save()

            profile.renter = form.cleaned_data['renter']
            profile.address = form.cleaned_data['address']
            profile.save()

            if form.cleaned_data['renter'] == False:
                puppy = Puppy.objects.filter(owner=request.user).first()
                if puppy:
                    puppy.delete()
            else:
                puppy.name = form.cleaned_data['name_of_dog'],
                puppy.breed = form.cleaned_data['breed_of_dog'],
                puppy.age = form.cleaned_data['age_of_dog']
                puppy.save()
            return redirect('/app/puppy/')
    else:
        data = {
            'firstname': request.user.first_name,
            'lastname': request.user.last_name,
            'email': request.user.email,
            'address': profile.address,
            'renter': profile.renter,
            'name_of_dog': '',
            'breed_of_dog': '',
            'age_of_dog': 0,
        }
        if puppy:
            data['name_of_dog'] = puppy.name,
            data['breed_of_dog'] = puppy.breed,
            data['age_of_dog'] = puppy.age

        form = ProfileForm(data)
        return render(request, 'pups/profile_edit.html', {'form': form})
