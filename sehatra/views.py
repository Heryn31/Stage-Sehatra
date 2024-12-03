# sehatra/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from datetime import datetime
from django.conf import settings
from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib import messages

User = get_user_model()

def home(request):
    concert_live_data = [{
        'title': "Revy Feu De Camp Mahaleo",
        'price': "15000Ar / 5,0€",
        'date' : "24 juin 2023",
        'duration': "1H",
        'genre': "Vazo Miteny",
        'image': "assets/images/concert_live/affiche-mahaleo.png",
        'detail':"Pour ce feu de camp, Dama et Bekoto seront accompagnés de Maharo (fils de Dama), Rôrô (fils de Charles), Benaivo (fils de Nônô), Pôpôly (Fils de Bekoto), Rado (fils de Fafah).",
        'description': "En 1982, le groupe Mahaleo avait fait un feu de camp diffusé sur la télévision nationale Malagasy. 40 ans plus tard, dans le cadre de la célébration du 50ème anniversaire du groupe, les deux membres restants accompagnés de leurs fils ont souhaité reproduire ce concept mais cette fois pour les Malagasy du monde entier."
    },
    {
        'title': "Revy Sy Vazo Miteny",
        'price': "25000Ar / 6,0€",
        'date': "10 septembre 2023",
        'duration': "4h 44min",
        'genre': "Vazo Miteny",
        'image': "assets/images/concert_live/vazo-miteny.png",
        'detail':"Samoela, Princio, et Rah-Chiky: En direct depuis Antsahamanitra le 10 Septembre 2023",
        'description': "Le trio Samoela, Princio, et Rah-Chiky entend se produire une nouvelle fois des années plus tard. Le spectacle s’intitule Revy sy Vazo Miteny. Préparez-vous à vibrer au son des chansons à texte les plus connues de Madagascar Les vazo miteny seront interprétés en trio, en duo, mais bien évidemment par l’auteur lui même",
    },
    {
        'title': "Ambondrona",
        'price': "30000Ar / 6,0€",
        'date': "25 février 2024",
        'duration': "3H",
        'genre': "Vazo Miteny",
        'image': "assets/images/concert_live/ambondrona.png",
        'detail':"Ambondrona - LIVE INÉDIT En direct du CCI Ivato",
        'description': "Leur premier grand concert pour 2024 !! Une playlist inédite",
    },
    {
        'title': "Revy Revy Mody Masoandro",
        'price': "15000Ar / 5,0€",
        'date': "28 juillet 2024",
        'duration': "4h 44min",
        'genre': "Traditionnel",
        'image': "assets/images/concert_live/revy-mody-masoandro.png",
        'detail':"Revy Revy Mody Masoandro avec Mahaleo, Benny & Bebey de Lolo sy ny tariny et Samoëla",
        'description': "Les légendes de la musique folk de Madagascar, ensemble sur une scène. Dama & Bekoto seront accompagnés par les Taranaka, Benny & Bebey par Nini Kolibera, et Samoëla par ses ingénieux musiciens En direct du parking de CCI Ivato le 28 Juillet 2024"
    },
    {
        'title': "Tarika Johary chante Barijaona & Kintana Telo",
        'price': "40000Ar / 8,0€",
        'date': "10 novembre 2024",
        'duration': "4H",
        'genre': "Traditionnel",
        'image': "assets/images/concert_live/johary.png",
        'detail':"Tarika Johary chante Barijaona & Kintana Telo. Lily, Lizah Raseta, Lilie, et Salomon, viendront enrichir ce moment de partage",
        'description': "Tarika Johary chante Barijaona & Kintana Telo - Une belle occasion de revivre des souvenirs nostalgiques à travers des chansons qui ont marqué des générations. Tarika Johary promet de faire résonner des mélodies qui rappellent les moments précieux de la vie. Lily, Lizah Raseta, Lilie, et Salomon, viendront enrichir ce moment de partage"
    }]
    
    movies_data = [
    {
        'title': "Unique Madagascar",
        'price': "20000Ar / 8,0€",
        'date' : "1 avril 2019",
        'production' : "Awesome Madagascar Tours",
        'duration': " 40 Min",
        'image': "assets/images/concert_live/unique.png",
        'description': "WHAT IS UNIQUE FOR YOU? UNIQUE IS SIMPLY THE ISLAND OF MADAGASCAR. Don't miss to watch this amazing video to explore its FIVE \"U\" -Unique wildlife like lemurs -Unique culture like playing with dead - Unique plant like baobab trees - Unique limestone rock formation like the Tsingy -Unique musical instruments like the Valiha."
     },
     {
        'title': "Sarango-pitia",
        'price': "5000Ar / 2,0€",
        'date' : "22 août 2023",
        'production' : "Film Malagasy novokarin'ny FR Production.",
        'duration': " 1h 08min",
        'image': "assets/images/films/sarangom-pitia-sehatra.png",
        'description': "Betsaka isika no niandry ny andiany fahadimy amin'ity andian-tantara Sarangom-pitia ity. Tsy nanaiky hatramin’ny farany i Mino ka voatery nanao sorona ny tenany, mety ho diso safidy ve izy ?"
     },
     {
        'title': "Sakaiza Mandoro",
        'price': "5000Ar / 2,0€",
        'date' : "22 août 2023",
        'production' : "Film Malagasy novokarin'ny FR Production.",
        'duration': " 1h 14min",
        'image': "assets/images/films/sakaiza-sehatra.png",
        'description': "Eto amin'ny SEHATRA.COM no hamoahana voalohany ity horonan-tsary vaovao ity. Atolotra am-pitiavana ho antsika mpanohana ny sarimihetsika Malagasy. Tantara-na ankizivavy nahita fianarana saingy voatery nanao mpiasa antrano tao amina mpanan-karena iray."
     },
      {
        'title': "Mafiady",
        'price': "5000Ar / 2,0€",
        'date' : "29 août 2023",
        'production' : " Watch Production",
        'duration': " 1h 20min",
        'image': "assets/images/films/Afiche_Mafiady-min.png",
        'description': "Film policier by Andry Rarivonandrasana."
     },
     {
        'title': "Le Mystère d'Arivonimamo",
        'price': "5000Ar / 2,0€",
        'date' : "04 décembre 2023",
        'production' : "Film Malagasy novokarin'ny FR Production.",
        'duration': " 26 Min",
        'image': "assets/images/films/mystere-d-arivonimamo.png",
        'description': "Chloe et Jehanne, deux adoléscentes passionnées de science, enquêtent sur le mystère des antennes qui composent le paysage d'Arivonimamo depuis des décenies. Ce qu'elles découvrent risque de changer l'avenir de Madagascar."
     }
    ]
    artiste_data = [{
        'name': "Samoela",
        'title': "Samoela En Live",
        'duration':"1h 10min",
        'date': "16 mai 2021",
        'price': "15000Ar / 5,0€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/samoela.png",
        'detail': "Concert realisé pendant la période de la Covid-19 à Madagascar.",
        'gender': "Vazo Miteny",
        'description':"Pendant plus d'une heure, Samoela et ses musiciens vous feront revivre ses 25 années de scènes pendant ce live.",
    },{
        'name': "Oladad",
        'title': "Oladad En Live",
        'duration':"1h 30min",
        'date': "29 mars 2023",
        'price': "15000Ar / 5,0€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/oladad.png",
        'detail': "Dadalo, Evans, Kids, Tsiry et Lova : ces Betsileo au grand talent de danseur et de chanteur (avec ses voix extraordinaires), vont vous faire voyager à travers la musique traditionnelle de Fianarantsoa fusionné par le rap",
        'gender': " hip-hop folk-fusion de Madagascar",
        'description': "Oladad est un groupe hip-hop folk-fusion de Madagascar. Ils interprètent une fusion de hip-hop, de danse et de le musique horija traditionnelle du peuple Betsileo, y compris des instruments comme le kabosy, jejy, sodina et le violon. Le groupe a été formé en 1996 à Fianarantsoa. Le groupe tire son nom de l’orthographe inverse du nom du membre principal Dadalo, dont le nom signifie 'chance' (vintana mahery adalo). Oladad comprend cinq chanteurs (Dadalao, Evans, Kids, Tsiry et Lova) et ses six musiciens. Dadalo, Evans, Kids, Tsiry et Lova : ces Betsileo au grand talent de danseur et de chanteur (avec ses voix extraordinaires), vont vous faire voyager à travers la musique traditionnelle de Fianarantsoa fusionné par le rap, les instruments telles que le kabosy, accordéon. Vivez le moment avec les chansons que vous connaissez tous : Afindrafindrao, Agnao, Ketamanga, Sesily, et bien beaucoup d’autres.",
    },
    {
        'name': "Tarika Sakelidalana",
        'title': "Live Sakelidalana",
        'duration':"50 Min",
        'date': "29 mars 2023",
        'price': "15000Ar / 5,0€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/sakelidalana.png",
        'detail': "Voahangy,Tao anatin'ny tolona,Fitia manalasala,Taratasin-drazandry et bien d'autres titres pendant ce live d'une heure",
        'gender': "Vazo Malagasy",
        'description': "Depuis que Rakotozanany Stanislas a quitté le groupe en 1980, on les connaît sous le nom de Tarika Sakelidalana. Le nom Sakelidalana a été tiré de la fameuse chanson 'Voahangy', que vous allez revivre dans ce spectacle, ainsi que d'autres harmonieuses compositions du groupe.",
    },
    {
        'name': "Vahantsaina",
        'title': "Vahantsaina One Man Band",
        'duration':"30 Min",
        'date': "1 mai 2023",
        'price': "13000Ar / 4,5€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/vahantsaina-couverture.png",
        'detail': "Vahantsaina un One Man Band vous fera découvrir ses compositions pendant ce live de trente minutes.",
        'gender': "Healing song et ses musiques engagées",
        'description': "Vahantsaina One Man Band nous invite à ce concert pour nous offrir un voyage musical particulier. L’homme-orchestre nous embarque en live avec ses healing song et ses musiques engagées. Il nous fascine en live en combinant le chant à trois voix, la guitare en accompagnement et en solo, la percussion émanant de sa propre guitare à 7 cordes, et surtout les mélodies envoutantes jaillissant de ses sodina. Tout cela réalisé par une seule personne. Laissez-vous emporter, bon visionnage.",
    },
    {
        'name': "Vilon'androy",
        'title': "Live Vilon'Androy",
        'duration':"1h 20min",
        'date': "13 mai 2023",
        'price': "20000Ar / 7,5€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/vilon-androy.png",
        'detail': "Spectacle tourné en pleine nature, danse typique de la région, des instruments vita malagasy, chansons acapella à 4 voix comme 'SALAKAO' que vous connaissez surement",
        'gender': "Musique du Grand-Sud",
        'description': "Un groupe du sud de l'île de Madagascar, mené par leur fameux chef de groupe Surgi, variant les styles Beko et Banaiky, de la musique typiquement malagasy grâce à laquelle Vilon'Androy a fait le tour du monde",
    }]
    return render(request, 'index.html', context={'artiste': artiste_data, 'concert_live': concert_live_data,'movies': movies_data,'request': request})

def pricing(request):
    return render(request, 'pricing.html', context={'request': request})

def concert_live(request):
    concert_live_data = [{
        'title': "Samoela En Live",
        'price': "15000Ar / 5,0€",
        'date' : "16 mai 2021",
        'genre': "Vazo Miteny",
        'image': "assets/images/concert_live/samoela.png",
        'description': "Pendant plus d'hune heure, Samoela et ses musiciens vous feront revivre ses 25 années de scènes pendant ce live."
    },
    {
        'title': "Tarika Johary chante Barijaona & Kintana Telo",
        'price': "40000Ar / 8,0€",
        'date': "10 novembre 2024",
        'genre': "Traditionnel",
        'image': "assets/images/concert_live/johary.png",
        'description': "Tarika Johary chante Barijaona & Kintana Telo - Une belle occasion de revivre des souvenirs nostalgiques à travers des chansons qui ont marqué des générations. Tarika Johary promet de faire résonner des mélodies qui rappellent les moments précieux de la vie. Lily, Lizah Raseta, Lilie, et Salomon, viendront enrichir ce moment de partage"
    },
    {
        'title': "Revy Revy Mody Masoandro",
        'price': "20000Ar / 6,5€",
        'date': "28 juillet 2024",
        'genre': "Traditionnel",
        'image': "assets/images/concert_live/revy-mody-masoandro.png",
        'description': "Revy Revy Mody Masoandro avec Mahaleo, Benny & Bebey de Lolo sy ny tariny et Samoëla. Les légendes de la musique folk de Madagascar, ensemble sur une scène. Dama & Bekoto seront accompagnés par les Taranaka, Benny & Bebey par Nini Kolibera, et Samoëla par ses ingénieux musiciens En direct du parking de CCI Ivato le 28 Juillet 2024"
    },
    {
        'title': "Tana Gospel Choir & Friends",
        'price': "15000Ar / 5,0€",
        'date': "30 mars 2024",
        'genre': "Evangelique",
        'image': "assets/images/concert_live/tgc-palais-des-sports.png",
        'description': "À l’occasion de son 20ème anniversaire, TGC invitent ses « Friends » : des chanteurs, des musiciens, des anciens membres, et vont se réunir à nouveau pour louer et célébrer. Vous aussi, vous êtes les friends de TGC , ils vous invitent ! Tana Gospel Choir - 20 ans TGC & Friends en direct du CCESCA le 30 Mars à 16h Heure de Madagascar"
    },
    ]
    return render(request, 'concert-live.html', context={'concert_live': concert_live_data,'request': request})

def movies(request):
    movies_data = [
    {
        'title': "Unique Madagascar",
        'price': "20000Ar / 8,0€",
        'date' : "1 avril 2019",
        'production' : "Awesome Madagascar Tours",
        'duration': " 40 Min",
        'image': "assets/images/concert_live/unique.png",
        'description': "WHAT IS UNIQUE FOR YOU? UNIQUE IS SIMPLY THE ISLAND OF MADAGASCAR. Don't miss to watch this amazing video to explore its FIVE "U" -Unique wildlife like lemurs -Unique culture like playing with dead - Unique plant like baobab trees - Unique limestone rock formation like the Tsingy -Unique musical instruments like the Valiha."
     },
     {
        'title': "Sarango-pitia",
        'price': "5000Ar / 2,0€",
        'date' : "22 août 2023",
        'production' : "Film Malagasy novokarin'ny FR Production.",
        'duration': " 1h 08min",
        'image': "assets/images/films/sarangom-pitia-sehatra.png",
        'description': "Betsaka isika no niandry ny andiany fahadimy amin'ity andian-tantara Sarangom-pitia ity. Tsy nanaiky hatramin’ny farany i Mino ka voatery nanao sorona ny tenany, mety ho diso safidy ve izy ?"
     },
     {
        'title': "Sakaiza Mandoro",
        'price': "5000Ar / 2,0€",
        'date' : "22 août 2023",
        'production' : "Film Malagasy novokarin'ny FR Production.",
        'duration': " 1h 14min",
        'image': "assets/images/films/sakaiza-sehatra.png",
        'description': "Eto amin'ny SEHATRA.COM no hamoahana voalohany ity horonan-tsary vaovao ity. Atolotra am-pitiavana ho antsika mpanohana ny sarimihetsika Malagasy. Tantara-na ankizivavy nahita fianarana saingy voatery nanao mpiasa antrano tao amina mpanan-karena iray."
     },
      {
        'title': "Mafiady",
        'price': "5000Ar / 2,0€",
        'date' : "29 août 2023",
        'production' : " Watch Production",
        'duration': " 1h 20min",
        'image': "assets/images/films/Afiche_Mafiady-min.png",
        'description': "Film policier by Andry Rarivonandrasana."
     },
     {
        'title': "Le Mystère d'Arivonimamo",
        'price': "5000Ar / 2,0€",
        'date' : "04 décembre 2023",
        'production' : "Film Malagasy novokarin'ny FR Production.",
        'duration': " 26 Min",
        'image': "assets/images/films/mystere-d-arivonimamo.png",
        'description': "Chloe et Jehanne, deux adoléscentes passionnées de science, enquêtent sur le mystère des antennes qui composent le paysage d'Arivonimamo depuis des décenies. Ce qu'elles découvrent risque de changer l'avenir de Madagascar."
     },
     ]
    return render(request, 'movies.html', context={'movies': movies_data,'request': request})

def artiste(request):
   artiste_data = [{
        'name': "Samoela",
        'title': "Samoela En Live",
        'duration':"1h 10min",
        'date': "16 mai 2021",
        'price': "15000Ar / 5,0€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/samoela.png",
        'detail': "Concert realisé pendant la période de la Covid-19 à Madagascar.",
        'gender': "Vazo Miteny",
        'description':"Pendant plus d'une heure, Samoela et ses musiciens vous feront revivre ses 25 années de scènes pendant ce live.",
    },{
        'name': "Oladad",
        'title': "Oladad En Live",
        'duration':"1h 30min",
        'date': "29 mars 2023",
        'price': "15000Ar / 5,0€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/oladad.png",
        'detail': "Dadalo, Evans, Kids, Tsiry et Lova : ces Betsileo au grand talent de danseur et de chanteur (avec ses voix extraordinaires), vont vous faire voyager à travers la musique traditionnelle de Fianarantsoa fusionné par le rap",
        'gender': " hip-hop folk-fusion de Madagascar",
        'description': "Oladad est un groupe hip-hop folk-fusion de Madagascar. Ils interprètent une fusion de hip-hop, de danse et de le musique horija traditionnelle du peuple Betsileo, y compris des instruments comme le kabosy, jejy, sodina et le violon. Le groupe a été formé en 1996 à Fianarantsoa. Le groupe tire son nom de l’orthographe inverse du nom du membre principal Dadalo, dont le nom signifie 'chance' (vintana mahery adalo). Oladad comprend cinq chanteurs (Dadalao, Evans, Kids, Tsiry et Lova) et ses six musiciens. Dadalo, Evans, Kids, Tsiry et Lova : ces Betsileo au grand talent de danseur et de chanteur (avec ses voix extraordinaires), vont vous faire voyager à travers la musique traditionnelle de Fianarantsoa fusionné par le rap, les instruments telles que le kabosy, accordéon. Vivez le moment avec les chansons que vous connaissez tous : Afindrafindrao, Agnao, Ketamanga, Sesily, et bien beaucoup d’autres.",
    },
    {
        'name': "Tarika Sakelidalana",
        'title': "Live Sakelidalana",
        'duration':"50 Min",
        'date': "29 mars 2023",
        'price': "15000Ar / 5,0€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/sakelidalana.png",
        'detail': "Voahangy,Tao anatin'ny tolona,Fitia manalasala,Taratasin-drazandry et bien d'autres titres pendant ce live d'une heure",
        'gender': "Vazo Malagasy",
        'description': "Depuis que Rakotozanany Stanislas a quitté le groupe en 1980, on les connaît sous le nom de Tarika Sakelidalana. Le nom Sakelidalana a été tiré de la fameuse chanson 'Voahangy', que vous allez revivre dans ce spectacle, ainsi que d'autres harmonieuses compositions du groupe.",
    },
    {
        'name': "Vahantsaina",
        'title': "Vahantsaina One Man Band",
        'duration':"30 Min",
        'date': "1 mai 2023",
        'price': "13000Ar / 4,5€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/vahantsaina-couverture.png",
        'detail': "Vahantsaina un One Man Band vous fera découvrir ses compositions pendant ce live de trente minutes.",
        'gender': "Healing song et ses musiques engagées",
        'description': "Vahantsaina One Man Band nous invite à ce concert pour nous offrir un voyage musical particulier. L’homme-orchestre nous embarque en live avec ses healing song et ses musiques engagées. Il nous fascine en live en combinant le chant à trois voix, la guitare en accompagnement et en solo, la percussion émanant de sa propre guitare à 7 cordes, et surtout les mélodies envoutantes jaillissant de ses sodina. Tout cela réalisé par une seule personne. Laissez-vous emporter, bon visionnage.",
    },
    {
        'name': "Vilon'androy",
        'title': "Live Vilon'Androy",
        'duration':"1h 20min",
        'date': "13 mai 2023",
        'price': "20000Ar / 7,5€",
        'nbr_video': "1",
        'image': "assets/images/concert_live/vilon-androy.png",
        'detail': "Spectacle tourné en pleine nature, danse typique de la région, des instruments vita malagasy, chansons acapella à 4 voix comme 'SALAKAO' que vous connaissez surement",
        'gender': "Musique du Grand-Sud",
        'description': "Un groupe du sud de l'île de Madagascar, mené par leur fameux chef de groupe Surgi, variant les styles Beko et Banaiky, de la musique typiquement malagasy grâce à laquelle Vilon'Androy a fait le tour du monde",
    }]
   return render(request, 'artiste.html', context={'artiste': artiste_data, 'request':request})
  
def organizers(request):
    organizers_data = [{
        'name':"awesone-madagascar-tours",
        'title': "Awesome Madagascar Tours",
        'duration':"40 Min",
        'price': "20000Ar / 8,0€",
        'date': "1 avril 2019",
        'nbr_video': "1",
        'image': "assets/images/concert_live/unique.png",
        'detail': "WHAT IS UNIQUE FOR YOU? UNIQUE IS SIMPLY THE ISLAND OF MADAGASCAR. Don't miss to watch this amazing video to explore its FIVE 'U' -Unique wildlife like lemurs -Unique culture like playing with dead - Unique plant like baobab trees - Unique limestone rock formation like the Tsingy -Unique musical instruments like the Valiha.",
        'description': "AWESOME MADAGASCAR TOURS est une entreprise locale de voyages malgaches fondée par l’équipe de mari et femme, Diary et Mihaja, qui sont dédiés à offrir des aventures incroyables aux voyageurs passionnés. Diary et Mihaja sont fiers de partager les talents naturels et l’histoire qu’ils ont hérités de leurs ancêtres pour s’assurer que votre séjour à Madagascar ne sera pas comme les autres.",
    }]
    return render(request, 'organizers.html', context={'organizers' : organizers_data, 'request': request})

def associations(request):
    associations_data = [{
        'name': "association-malgache-pour-lautisme",
        'title': "Association Malgache pour l'Autisme",
        'image': "assets/images/concert_live/couverture-ama.png",
        'action': "Action Sociale",
        'nbr_action': "1",
        'description': "L’Association Malgache pour l’Autisme (AMA) est une association des parents, familles et amis de personnes autistes et de professionnels relevant du domaine de l’autisme. Elle est née à la suite d’une prise de conscience de quelques parents d’autistes de la nécessité de s’organiser pour faire avancer la cause des personnes vivant avec autisme à Madagascar."
    }]
    return render(request, 'associations.html', context={'associations' : associations_data,'request': request})

def artiste_details(request, name):
    artiste_data = {
        'name': "mahaleo-en-live",
        'title': "Mahaleo",
        'date': "20-09-2024",
        'detail': "Musique Malagasy",
        'partner': "Artiste",
        'about_partner': "À propos de l'artiste",
        'nbr_action': "1",
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
        'detail_action':"Nous sommes conscients de la nécessité de soutenir les autistes pour qu’ils puissent mettre en valeur leur potentiel et qu’ils puissent exercer leur droit fondamental à l’égalité des chances et au bien-être. Notre objectif fondamental est qu’ils pourront grandir dans une société davantage accessible, où ils pourront s’épanouir et accéder à l’autonomie.",
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
       
    }
    video_url = f"{settings.MEDIA_URL}test.mp4"
    return render(request, 'single-movie.html', context={'data': single_movie_data,'name': name ,'video_url': video_url ,'request': request})

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
        'name': 'Example Name',  
        'title': 'Example Title', 
        'action': "Action Sociale",
        'date': datetime.now().strftime('%d/%m/%Y %H:%M')  
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


def custom_login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        print(username,password)
        if user is not None:
            login(request, user)
            messages.success(request,"Connexion réussie ! Bienvenue "+username.capitalize()+".")
            return redirect("/")
        else:
            messages.error(request, "Erreur de connection")
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

        print(username,email,password,confirm_password)
        
        # Validate that the password and confirm_password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("home")  # Redirect back to the sign-up page if they don't match
        
        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("home")  # Redirect back to the sign-up page if the username exists
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("home")  # Redirect back to the sign-up page if the email exists

        # Create the new user and save to the database, password is automatically hashed
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print("Creating the account")
        # Log the user in after creating the account
        login(request, user)

        print("User Logged")

        # Show a success message and redirect to a desired page (e.g., home)
        messages.success(request, "Account created and logged in successfully!")
        return redirect("/") 

    return render(request, "index.html")