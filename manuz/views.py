from datetime import date

from django.shortcuts import render
from . models import Post





def home(request):
  context= {
    'posts': Post.objects.all()
  }
  return render(request, 'manuz/home.html', context)


def about(request):
  return render(request, 'manuz/about.html', {'title': 'About'})

