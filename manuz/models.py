from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# # Create your models here.
class Post(models.Model):
  image = models.ImageField()
#   title = models.CharField(max_length=100)
#   content = models.TextField(max_length=225, null=True)
#   likes = models.IntegerField(null=True, default=0)
#   date_posted = models.DateTimeField(default=timezone.now)
#   author = models.ForeignKey(User, on_delete=models.CASCADE) 
  
#   def __str__(self):
#         return self.title

#   # def save_post(self):
#         # self.save()

#   # def delete_post(self):
#         # self.delete()