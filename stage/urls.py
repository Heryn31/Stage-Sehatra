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
    path('pricing/', views.pricing, name='pricing'), 
    path('movies/', views.movies, name='movies'), 
    path('single-movie/', views.single_movie, name='single_movie'),  
    path('single-actor/', views.single_actor, name='single_actor'),  
    path('tv-shows/', views.tv_shows, name='tv_shows'), 
    path('blog/', views.blog, name='blog'),
    path('single-post/', views.single_post, name='single_post'),  
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),  
    path('faq/', views.faq, name='faq'),  # Page FAQ
    path('coming-soon/', views.coming_soon, name='coming_soon'),  
    path('404/', views.error_404, name='404'), 
    path('profile-account/', views.profile_account, name='profile_account'),  
    path('favorite/', views.favorite, name='favorite'),  
    path('reviews/', views.reviews, name='reviews'),  
    path('edit-account/', views.editAccount, name='edit_account'),
    path('notification/', views.notification, name='notification'),
]
