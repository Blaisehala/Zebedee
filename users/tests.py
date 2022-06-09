from django.test import TestCase
from django.test import TestCase
from .models import Comment, Post, Profile 

# Create your tests here.

class CommentTestCass(TestCase):
  #set up method
  def setUp(self):
    self.jiji = Post(post='jiji')
    self.message= Comment(comment='wow', post=self.jiji)

  def test_instance(self):
    self.assertTrue(isinstance(self.message,Comment))

  def test_save_method(self):
    self.message.save_post()
    comments = Comment.objects.all()
    self.assertTrue(len(comments) > 0)

  def tearDown(self):
    Comment.objects.all().delete()

class PostTestClass(TestCase):
  def setUp(self):
    self.firstpost= Post (image='http://', title='hah', post='hehe',caption='jiji',likes=2)
  def test_instance(self):
    self.assertTrue(isinstance(self.firstpost,Post))

class ProfileTestClass(TestCase):
  def setUp(self):
    self.profilic = Profile(image='http://')
  def test_instance(self):
    self.assertTrue(isinstance(self.profilic,Profile))
 

