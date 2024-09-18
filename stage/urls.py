"""
URL configuration for stage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# stage/urls.py

from django.contrib import admin
from django.urls import path
from sehatra import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('abonnement/', views.pricing, name='pricing'), 
    path('concert-live/', views.concert_live, name='concert_live'), 
    path('film/', views.movies, name='movies'), 
    path('video-film/', views.single_movie, name='single_movie'),  
    path('artiste/', views.artiste, name='artiste'),
    path('artiste/nom', views.single_artiste, name='single_artiste'), # [Nom] change le nom d'artiste
    path('organisateur/', views.organizers, name='organizers'),
    path('association/', views.associations, name='associations'),
    

    path('blog/', views.blog, name='blog'),
    path('single-post/', views.single_post, name='single_post'),  
    path('a-propos/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),  
    path('question/', views.faq, name='faq'),  
    path('a-venir/', views.coming_soon, name='coming_soon'),  
    path('404/', views.error_404, name='404'), 
    path('profil-compte/', views.profile_account, name='profile_account'),  
    path('favoris/', views.favorite, name='favorite'),  
    path('avis-commentaires/', views.reviews, name='reviews'),  
    path('modification-compte/', views.editAccount, name='edit_account'),
    path('notification/', views.notification, name='notification'),
]
