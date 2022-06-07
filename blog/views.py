from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from blog.models import *


def index(request):
    return render(request, 'index.html')


def foto(request):
    return render(request, 'foto.html')



def video(request):
    return render(request, 'video.html')


def Get_Product(request):
    product = Product
    context = {
      'pr': product
    }
    return render(request, 'KUTUBXONA YANGILIKLARI.html')
  
   
   



def word(request):
    return render(request, 'word.html')


def about(request):
    return render(request, 'about.html')


def ADOUT(request):
    return render(request, 'ADOUT.html')


def contact(request):
    return render(request, 'contact.html')
