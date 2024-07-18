from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Products
from django.urls import reverse_lazy

# Create your views here.
def Home(request):
    user = request.user
    return render(request, 'main/home.html', {'user': user})


class Shop(ListView):
    model = Products
    template_name = 'main/shop.html'


class Detail(DetailView):
    model = Products
    template_name = 'main/detail.html'


class Create(CreateView):
    model = Products
    template_name = 'main/newpost.html'
    fields = ['name', 'description', 'price', 'author']


class Edit(UpdateView):
    model = Products
    template_name = 'main/postedit.html'
    fields = ['description', 'price']    


class Delete(DeleteView):
    model = Products
    template_name = 'main/postdelete.html'
    success_url = reverse_lazy('shop')