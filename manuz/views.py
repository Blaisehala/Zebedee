from datetime import date
from multiprocessing import context
from django.shortcuts import render

posts = [
  {
    'author': 'Blaise',
    'title': 'Post1',
    'image': 'pic1',
    'date': 'August 10',
  },
   {
    'author': 'Blaise',
    'title': 'Post2',
    'image': 'pic1',
    'date': 'August 11',
  },


]


def home(request):
  context= {
    'posts': posts
  }
  return render(request, 'manuz/home.html', context)


def about(request):
  return render(request, 'manuz/about.html', {'title': 'About'})

