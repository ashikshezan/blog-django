from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  )
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.views import generic


class BlogHomeView(ListView):
    template_name = 'posts/home.html'
    model = Post


class BlogDetailView(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post


class BlogNewPostView(CreateView):
    template_name = 'posts/new_post.html'
    model = Post
    fields = '__all__'


class BlogUpdatePostView(UpdateView):
    template_name = 'posts/update_post.html'
    model = Post
    fields = ['title', 'content']


class BlogDeletePostView(DeleteView):
    template_name = 'posts/delete_post.html'
    model = Post
    success_url = reverse_lazy('home')


class BlogSignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'posts/signup.html'
