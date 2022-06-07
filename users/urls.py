from django.urls import path
# from . import views 


from . views import AddPostView


urlpatterns = [
    
    path('newpost/',AddPostView.as_view(),name='newpost'),
]
