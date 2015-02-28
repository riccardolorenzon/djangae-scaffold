from forms import BlogArticleForm, CommentForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import BlogArticle, ImageBlogArticle
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# index
def index(request):
    blog_objects = BlogArticle.objects.all().order_by()
    paginator = Paginator(blog_objects, 5)
    page = request.GET.get('page')
    try:
        blog_objects = paginator.page(page)
    except PageNotAnInteger:
        blog_objects = paginator.page(1)
    except EmptyPage:
        blog_objects = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password)
        if user != None:
            login(request,user)
            response = render(request, "./blogtemplate.html", {"testvar" : "test string", "blogs" : blog_objects, "user" : user} )
            return response
    response = render(request, "./blogtemplate.html", {"testvar" : "test string", "blogs" : blog_objects} )
    return response

# create blog view
def createblog(request):
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.author = request.user
    newBlog.blog_content = request.POST['blog_content']
    newBlog.save()
    return HttpResponseRedirect('/')

def update_article(request):
    if request.method == 'POST':
        article_id = request.POST['editBlogArticleId']
        blog = BlogArticle.objects.get(id = article_id)

        if blog != None and request.user == blog.author:
            blog.title = request.POST['title']
            blog.blog_content = request.POST['content']
            blog.save()
    return HttpResponseRedirect("/")

def delete_article(request, article_id):
    blog = BlogArticle.objects.get(id = article_id)
    deleted = True
    if blog == None or request.user != blog.author:
        deleted = False
    else:
        blog.delete()
    return HttpResponseRedirect("/")

def upload_image(request):
    blog = BlogArticle.objects.filter(id = request.POST['blogArticleId'])
    if request.user == blog.author:
        new_sharedimage = ImageBlogArticle()
        new_sharedimage.image = request.FILES['file']
        new_sharedimage.blogarticle_id = request.POST['blogArticleId']
        new_sharedimage.title = request.POST['title']
        new_sharedimage.description = request.POST['description']
        new_sharedimage.save()
    return HttpResponseRedirect("/")

def delete_image(request, article_id, image_id):
    current_user = request.user
    image = ImageBlogArticle.objects.get(id = image_id)
    if (image.blogarticle.author == current_user):
        image.delete()
    return HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
