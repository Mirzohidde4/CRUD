from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Edit(generic.UpdateView):
    model = User
    template_name = 'registration/settings.html'
    fields = ['first_name', 'last_name']  
    success_url = reverse_lazy('home')  


class Delete(generic.DeleteView):
    model = User
    template_name = 'registration/deleteaccount.html'
    success_url = reverse_lazy('home')