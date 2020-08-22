import os
import random
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = 'feny'
    return HttpResponse(os.listdir(f'./amigos/static/img/{name}'))

def amigo(response ,name):
    photos = os.listdir(f'./amigos/static/img/{name}')
    photos +=photos[:]
    random.shuffle(photos)
    for i in range(len(photos)):
        photos[i] = 'img/' + name + '/' + photos[i]
    return render(response, "amigo/index.html", {
        "name":name.lower(),
        "photos": photos
    })