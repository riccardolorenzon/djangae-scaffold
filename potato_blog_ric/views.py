from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from models import BlogArticle, ImageBlogArticle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from google.appengine.api import users

# index
def index(request):
    blog_articles_objects = BlogArticle.objects.all().order_by("-created_on")
    paginator = Paginator(blog_articles_objects, 5)
    page = request.GET.get('page')
    try:
        blog_articles_objects = paginator.page(page)
    except PageNotAnInteger:
        blog_articles_objects = paginator.page(1)
    except EmptyPage:
        blog_articles_objects = paginator.page(paginator.num_pages)
    response = render(request, "./blogtemplate.html", {"blog_articles" : blog_articles_objects, "login_url": users.create_login_url('/'), "logout_url": users.create_logout_url('/')})
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
        blog_article = BlogArticle.objects.get(id = article_id)

        if blog_article != None and request.user == blog_article.author:
            blog_article.title = request.POST['title']
            blog_article.blog_content = request.POST['content']
            blog_article.save()
    return HttpResponseRedirect("/")

def delete_article(request, article_id):
    blog_article = BlogArticle.objects.get(id = article_id)
    deleted = True
    if blog_article == None or request.user != blog_article.author:
        deleted = False
    else:
        blog_article.delete()
    return HttpResponseRedirect("/")

def upload_image(request):
    blog_article = BlogArticle.objects.get(id = request.POST['blogArticleId'])
    if request.user == blog_article.author:
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
