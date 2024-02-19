from django.urls import path
from .views import *

urlpatterns  = [
    path('', home, name = 'home'),
    path('more/', More_page, name= 'more'),
    path('discord/', Discords, name= 'discord'),
    path('online/', Online, name= 'online'),
    path('savdo/', Robot, name='savdo'),
    path('cultor/',  calculator, name='cultor'),

]