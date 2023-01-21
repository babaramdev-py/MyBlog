from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,DetailView
                                  ,CreateView,UpdateView,DeleteView)
from blog.models import *
from blog.forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin # analogous to login_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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
    model = Post
    login_url = '/login/' #if  not logged go to /login
    redirect_field_name = 'blog/post_list.html' #
    form_class = PostForm





class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    login_url = '/login/' #if  not logged go to /login
    redirect_field_name = 'blog/post_detail.html' #
    form_class = PostForm

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
    

# 
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk = comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_list')