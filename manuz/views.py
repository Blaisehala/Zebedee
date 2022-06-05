from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Axels  Home 123</h1>')


def about(request):
  return HttpResponse('<h1>Axels About 456</h1>')

