# sehatra/views.py

from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def home(request):
    return render(request, 'index.html', context={'request': request})

def pricing(request):
    return render(request, 'pricing.html', context={'request': request})

def concert_live(request):
    concert_live_data = {
        'title': "Samoela En Live",
        'price': "15000Ar / 5,0€"
    }
    return render(request, 'concert-live.html', context={'concert_live': concert_live_data,'request': request})

def movies(request):
    return render(request, 'movies.html', context={'request': request})

def artiste(request):
   artiste_data = [{
        'name': "mahaleo",
        'title': "Mahaleo",
        'date': "20-09-2024",
        'detail': "Musique Malagasy"
    },{
        'name': "samoela",
        'title': "Samoela",
        'date': "20-09-2024",
        'detail': "Musique Malagasy"
    }]
   return render(request, 'artiste.html', context={'artiste': artiste_data, 'request':request})
  
def organizers(request):
    organizers_data = [{
        'name': "awesome-madagascar-tours",
        'title': "Awesome Madagascar Tours",
        'date': "01-04-2024",
        'views': '40M'
    }]
    return render(request, 'organizers.html', context={'organizers' : organizers_data, 'request': request})

def associations(request):
    associations_data = [{
        'name': "awesome-madagascar-tours",
        'title': "Association Malgache pour l'Autisme",
        'action': "Action Sociale"
    }]
    return render(request, 'associations.html', context={'associations' : associations_data,'request': request})

def artiste_details(request, name):
    # Données de l'artiste
    artiste_data = {
        'name': "mahaleo-en-live",
        'title': "Mahaleo",
        'date': "20-09-2024",
        'detail': "Musique Malagasy",
        'partner': "Artiste",
        'about_partner': "À propos de l'artiste",
        'nbr_video': "1",
        'associate':"Vidéos associées à cette artiste",
        'duration': "1h 56min",
        'other': "Les autres artistes présents sur SEHATRA"
    }
    return render(request, 'partner-details.html', context={'data': artiste_data, 'type': 'artiste', 'request': request, 'name': name})

def organizers_details(request, name):
    # Données de l'organisateur
    organizers_data = {
        'name':"awesone-madagascar-tours",
        'title': "Awesome Madagascar Tours",
        'date': "01-04-2024",
        'detail': "AWESOME MADAGASCAR TOURS est une entreprise locale de voyages malgaches fondée par l’équipe de mari et femme, Diary et Mihaja, qui sont dédiés à offrir des aventures incroyables aux voyageurs passionnés. Diary et Mihaja sont fiers de partager les talents naturels et l’histoire qu’ils ont hérités de leurs ancêtres pour s’assurer que votre séjour à Madagascar ne sera pas comme les autres.",
        'views': '40M',
        'partner': "Organisateur",
        'about_partner': "À propos de l'organisateur",
        'nbr_video': "1",
        'associate':"Vidéos associées à cet organisateur",
        'duration': "1h 30min",
        'other': "Les autres organisateurs présents sur SEHATRA"
    }
    return render(request, 'partner-details.html', context={'data': organizers_data, 'type': 'organizer', 'request': request, 'name': name})

def association_details(request, name):
    associations_data = {
        'name': "association-malgache-pour-l'autisme",
        'title': "Association Malgache pour l'Autisme",
        'date': "06-09-2024",
        'action': "Action Sociale",
        'detail': "L’Association Malgache pour l’Autisme (AMA) est une association des parents, familles et amis de personnes autistes et de professionnels relevant du domaine de l’autisme. Elle est née à la suite d’une prise de conscience de quelques parents d’autistes de la nécessité de s’organiser pour faire avancer la cause des personnes vivant avec autisme à Madagascar.",
        'partner': "Association",
        'about_partner': "À propos de l'association",
        'nbr_video': "1",
        'associate':"Vidéos associées à cette action",
        'duration': "1h 30min",
        'other': "Les autres associations présents sur SEHATRA"
    }
    return render(request, 'partner-details.html', context={'data': associations_data, 'type': 'association', 'request': request, 'name': name})

def partner_details(request):
    return render(request, 'partner-details.html', context={'request': request})

def single_movie(request, name):
    single_movie_data = {
        'name': "single-movie"
    }
    return render(request, 'single-movie.html', context={'data': single_movie_data,'name': name ,'request': request})

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
    reviews_data = [{
        'name': 'Example Name',  # Remplacez par la valeur souhaitée
        'title': 'Example Title',  # Remplacez par la valeur souhaitée
        'action': "Action Sociale",
        'date': datetime.now().strftime('%d/%m/%Y %H:%M')  # Ajout de la date et l'heure
    }]
    return render(request, 'account-reviews.html', context={'reviews': reviews_data, 'request': request})

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