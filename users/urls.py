from django.urls import path
from . import views 


from . views import AddPostView


urlpatterns = [
    path('', views.home, name='axel-home'),
    path('about/', views.about, name='axel-about'),
    path ('newpost/',views.new_post, name='newpost'),
    
     
]