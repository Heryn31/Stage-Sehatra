# sehatra/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def movies(request):
    return render(request, 'movies.html')
def single_movie(request):
    return render(request, 'single-movie.html')

def single_actor(request):
    return render(request, 'single-actor.html')

def tv_shows(request):
    return render(request, 'tv-shows.html')

def blog(request):
    return render(request, 'blog.html')

def single_post(request):
    return render(request, 'single-post.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')

def coming_soon(request):
    return render(request, 'coming-soon.html')

def error_404(request):
    return render(request, '404.html')