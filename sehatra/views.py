# sehatra/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json
import os
from datetime import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

User = get_user_model()


def load_json_data(filename):
    file_path = os.path.join(settings.BASE_DIR, 'static', 'data', filename)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def home(request):
    data = load_json_data('fakedata.json')
    return render(request, 'index.html', context={'concert_live': data.get('concert_live', []), 'movies': data.get('movies', []), 'artiste': data.get('artiste', []), 'request': request})


def pricing(request):
    return render(request, 'pricing.html', context={'request': request})


def concert_live(request):
    data = load_json_data('fakedata.json')
    return render(request, 'concert-live.html', context={'concert_live': data.get('concert_live', []), 'request': request})


def movies(request):
    data = load_json_data('fakedata.json')
    return render(request, 'movies.html', context={'movies': data.get('movies', []), 'request': request})


def artiste(request):
    data = load_json_data('fakedata.json')
    return render(request, 'artiste.html', context={'artiste': data.get('artiste', []), 'request':request})

  
def organizers(request):
    data = load_json_data('fakedata.json')
    return render(request, 'organizers.html', context={'organizers': data.get('organizers', []), 'request': request})


def associations(request):
    data = load_json_data('fakedata.json')
    return render(request, 'associations.html', context={'associations': data.get('associations', []), 'request': request})


def artiste_details(request, name):
    data = load_json_data('fakedata.json')
    # Find the artist by name
    artiste = next((art for art in data.get('artiste', []) if art['name'] == name), None)
    return render(request, 'partner-details.html', context={'data': artiste, 'type': 'artiste', 'request': request, 'name': name})


def organizers_details(request, name):

    data = load_json_data('fakedata.json')
    # Find the organizers by name
    organizer = next((org for org in data.get('organizers', []) if org['name'] == name), None)
    return render(request, 'partner-details.html', context={'data': organizer, 'type': 'organizer', 'request': request, 'name': name})


def association_details(request, name):
    data = load_json_data('fakedata.json')
    # Find the association by name
    association = next((ass for ass in data.get('associations', []) if ass['name'] == name), None)
    return render(request, 'partner-details.html', context={'data': association, 'type': 'association', 'request': request, 'name': name})


def partner_details(request):
    return render(request, 'partner-details.html', context={'request': request})


def single_movie(request, name):
    single_movie_data = {
       "name":"samoela",
    }
    video_url = f"{settings.MEDIA_URL}test.mp4"
    return render(request, 'single-movie.html', context={'data': single_movie_data,'name': name ,'video_url': video_url ,'request': request})
    # data = load_json_data('fakedata.json')
    
    # # Recherche des éléments correspondants dans les différentes catégories
    # concert_live = next((concert_live for concert_live in data.get('concert_live', []) if concert_live['title'].lower() == name.lower()), None)
    # movies = next((movie for movie in data.get('movies', []) if movie['title'].lower() == name.lower()), None)
    # artiste = next((artiste for artiste in data.get('artiste', []) if artiste['title'].lower() == name.lower()), None)
    # organizers = next((organizers for organizers in data.get('organizers', []) if organizers['title'].lower() == name.lower()), None)
    # associations = next((associations for associations in data.get('associations', []) if associations['title'].lower() == name.lower()), None)

    # # Construire l'URL du fichier vidéo
    # video_url = f"{settings.MEDIA_URL}test.mp4"
    
    # # Passer les données dans le contexte sous forme de dictionnaire unique
    # return render(request, 'single-movie.html', context={
    #     'name': name,
    #     'video_url': video_url,
    #     'request': request
    # })

def about(request):
    return render(request, 'about.html', context={'request': request})


def contact(request):
    return render(request, 'contact.html', context={'request': request})


def faq(request):
    return render(request, 'faq.html', context={'request': request})


def coming_soon(request):
    return render(request, 'coming-soon.html', context={'request': request})


def error_404(request):
    return render(request, '404.html', context={'request': request})


def profile_account(request):
    return  render(request, 'account-profile.html', context={'request': request})


def favorite(request):
    return render(request, 'account-favorites.html', context={'request': request})

 
def reviews(request):
    return render(request, 'account-reviews.html', context={ 'request': request})

def editAccount(request):
    return render(request, 'account-edit.html', context={'request': request})


def notification(request):
    return render(request, 'account-notifications.html', context={'request': request})


def base(request):
    return render(request, 'base.html', context={'request': request})


def navbartop(request):
    return render(request, 'navbar-top.html', context={'request': request})


def footer(request):
    return render(request, 'footer.html', context={'request': request})


def privacy(request):
    return render(request, 'privacy.html', context={'request': request})


def terms(request):
    return render(request, 'terms.html', context={'request': request})


def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            messages.success(request, "Connexion réussie ! Bienvenue " + username.capitalize() + ".")
            return redirect("/")
        else:
            messages.error(request, "Erreur de connection,vérifier votre informations")
            return redirect("/")

    return render(request, "index.html")


def custom_logout_view(request):
    if request.user.is_authenticated:
        # Set user as offline in the database before logging out
        user = request.user
        user.is_online = False
        user.save()
        
        # Log the user out
        logout(request)
        messages.success(request, "Vous avez été déconnecté avec succès.")
        return redirect("/")
    
    return redirect("/")


def custom_signup_view(request):
    if request.method == "POST":
        # Collect user data from the form
        username = request.POST.get("sp_name")
        email = request.POST.get("sp_email")
        password = request.POST.get("sp_password")
        confirm_password = request.POST.get("sp_password_confirmation")

        print(username, email, password, confirm_password)
        
        # Validate that the password and confirm_password match
        if password != confirm_password:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect("home")  # Redirect back to the sign-up page if they don't match
        
        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Le nom d'utilisateur existe déjà.")
            return redirect("home")  # Redirect back to the sign-up page if the username exists
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "L'Email existe déjà.")
            return redirect("home")  # Redirect back to the sign-up page if the email exists

        # Create the new user and save to the database, password is automatically hashed
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("Creating the account")
        # Log the user in after creating the account
        login(request, user)

        print("User Logged")

        # Show a success message and redirect to a desired page (e.g., home)
        messages.success(request, "Compte créé et connecté avec succès !")
        return redirect("/") 

    return render(request, "index.html")
