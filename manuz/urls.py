from django.urls import path
from . import views 



urlpatterns = [
    path('', views.home, name='axel-home'),
    path('about/', views.about, name='axel-about'),
    
]