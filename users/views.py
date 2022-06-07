from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth.decorators import login_required

from users.models import post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django. views.generic import CreateView


# Create your views here.
def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}.You can Login')
      return redirect ('login')


  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
   if request.method == 'POST':
     u_form = UserUpdateForm(request.POST, instance=request.user)
     p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

     if u_form.is_valid() and p_form.is_valid():
       u_form.save()
       p_form.save()
       messages.success(request, f'Account updated succefully.')
       return redirect('profile')

   else:
     u_form = UserUpdateForm(instance=request.user)
     p_form = ProfileUpdateForm(instance=request.user.profile)



   context = {
    'u_form': u_form,
    'p_form': p_form,
  }
  
   return render(request, 'users/profile.html', context)

  

class AddPostView(CreateView):
  model = post
  template_name = 'newpost.html'
  fields = ['title', 'caption', 'image']

  def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

