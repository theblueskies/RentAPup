import json

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

from pups.models import Puppy


def index(request):
    puppies = Puppy.objects.all()
    template = loader.get_template('pups/index.html')
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


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        print (request.data)
        return HttpResponse(json.dumps(request.data))
