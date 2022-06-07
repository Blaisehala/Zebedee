from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from users.models import *
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
  user= models.OneToOneField(User, on_delete=models.CASCADE)
  image= models.ImageField(default='default.jpg', upload_to='profile_pics')

def __str__(self):
  return f'{self.user.username} Profile'


class Post(models.Model):
  image=models.ImageField(upload_to = 'profile_pics', default='no image')
  title = models.CharField(max_length=100, default='')
  post = HTMLField(null=True)
  caption = models.TextField(max_length=300, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
  likes=models.IntegerField(null=True, default=0)
  pub_date = models.DateTimeField(default=timezone.now)
  
  
  def __str__(self):
    return self.caption
    
    
  def save_post(self):
    self.save()

  def delete_post(self):
    self.delete()

class Comment(models.Model):
  comment = models.TextField()
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
  date = models.DateTimeField(auto_now_add=True, null=True)
  
  
  def __str__(self):
    return f'{self.user.name} post'







