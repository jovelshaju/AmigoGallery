import os
import random
from django.urls import reverse
from django import forms
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms

class LoginForm(forms.Form):
   name = forms.CharField(max_length = 100)

def index(request):
    if request.method == "POST":
      MyLoginForm = LoginForm(request.POST)

      if MyLoginForm.is_valid():
        name = MyLoginForm.cleaned_data['name']
        return HttpResponseRedirect(reverse("index")+name)

    else:
        return render(request, "home/index.html")

def amigo(response ,name):
    if(name.isalpha()):
        name = name.lower()
        if(os.path.exists(f'./AmigoGallery/static/amigo/img/{name}')):
            photos = os.listdir(f'./AmigoGallery/static/amigo/img/{name}')
            photos +=photos[:]
            random.shuffle(photos)
            for i in range(len(photos)):
                photos[i] = 'amigo/img/' + name + '/' + photos[i]
            return render(response, "amigo/index.html", {
                "name":name,
                "photos": photos
            })
        else:
            return render(response, "404/index.html", {
                "name":name
            })
    else:
        return HttpResponseRedirect(reverse('index'))