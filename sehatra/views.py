# sehatra/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def pricing(request):
    return render(request, 'pricing.html')

def concert_live(request):
    return render(request, 'concert-live.html')

def movies(request):
    return render(request, 'movies.html')

def artiste(request):
    return render(request, 'artiste.html')

def organizers(request):
    return render(request, 'organizers.html')

def associations(request):
    return render(request, 'associations.html')


def single_movie(request):
    return render(request, 'single-movie.html')

def single_artiste(request):
    return render(request, 'single-artiste.html')

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

def profile_account(request):
    return  render(request, 'account-profile.html')

def favorite(request):
    return render(request, 'account-favorites.html')

def reviews(request):
    return render(request, 'account-reviews.html')

def editAccount(request):
    return render(request, 'account-edit.html')

def notification(request):
    return render(request, 'account-notifications.html')

def log_out(request):
    return render(request, 'index.html')
