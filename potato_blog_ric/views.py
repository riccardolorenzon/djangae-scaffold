from django.shortcuts import render
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

from models import Post
from forms import PostForm, CommentForm

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello my beautiful blog!!')

def add_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponse('post inserted successully')
    return render_to_response('add_post.html',
                              { 'form': form },
                              context_instance=RequestContext(request))

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render_to_response('blog_post.html',
                              {
                                  'post': post,
                                  'form': form,
                              },
                              context_instance=RequestContext(request))