from django.shortcuts import render
from django.views.generic import (TemplateView,ListView,DetailView
                                  ,CreateView,UpdateView,DeleteView)
from blog.models import *
from blog.forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin # analogous to login_required
from django.urls import reverse_lazy
# Create your views here.




class AboutView(TemplateView):
    template_name = 'about.html'



# List of all the posts
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    


class PostDetailView(DetailView):
    model = Post



# Only for a logged in user! In FBV's we used decorators, use something use to
# authenticate
# Django Mixins help us to authenticate, they are like decorators like @login_required


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/' #if  not logged go to /login
    redirect_field_name = 'blog/post_detail.html' #
    form_class = PostForm
    model = Post




class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/' #if  not logged go to /login
    redirect_field_name = 'blog/post_detail.html' #
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    # dont activate delete url until actually deleted
    success_url = reverse_lazy('post_list')




class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/' #if  not logged go to /login
    redirect_field_name = 'blog/post_list.html' #
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull = True).order_by('created_date')