from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('counter', views.counter, name='counter'),
    path('wordcount', views.wordcount, name='wordcount'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post') # for dynamic url rendering
]