from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import RegistrationModelForm, PostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from datetime import datetime

# Create your views here.
def index(request):
    context = {}
    posts = Post.objects.all().order_by('-id')
    context['posts'] = posts
    return render(request, 'index.html', context)


@login_required
def create(request):
    context = {}
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:index')
        else:
            context['form'] = form
            return render(request, 'create.html', context)
    else:
        context['form'] = PostModelForm(initial={'date_created': datetime.now().date()})
        return render(request, 'create.html', context)


@login_required
def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=post_id)
    return render(request, 'detail.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:index')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
        return render(request, 'update.html', context)

def delete(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.delete()
            return redirect('post:index')
    else:
        post = Post.objects.get(id=post_id)
        context = {}
        context['form'] = PostModelForm(instance=post)
        return render(request, 'index.html', context)
    

def registration(request):
    form = RegistrationModelForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = RegistrationModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password'])
            user.save()
            login(request, user)
            return redirect('post:index')
        else:
            context['form'] = form
    return render(request, 'registration.html', context)


def user_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('post:index')
    return render(request, 'login.html', context)


def user_logout(request):
    context = {}
    logout(request)
    return redirect('post:index')