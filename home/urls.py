from django.contrib import admin
from django.urls import path,include,re_path
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('events/', views.events,name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('contactus/', views.contactus, name='contactus'),
    path('aboutIEI/', views.aboutIEI,name='aboutIEI'),
    path('about/history/', views.about_history,name='about_history'),
    path('about/vision/', views.about_vision,name='about_vision'),
    path('about/team/', views.about_team,name='about_team'),
    path('about/alumni/', views.about_alumni,name='about_alumni'),
    path('aboutIEI/membership/', views.aboutIEI_membership,name='aboutIEI_membership'),
    path('aboutIEI/benefits/', views.aboutIEI_benefits,name='aboutIEI_benefits'),
    
    
]
