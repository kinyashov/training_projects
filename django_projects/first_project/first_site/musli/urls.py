from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('performer/', views.all_performer, name='all_performer'),
    path('performer/?sort=<sort>', views.all_performer, name='all_performer'),
    path('performer/<slug:slug_performer>/', views.performer, name='performer'),
    path('genre/', views.all_genre, name='all_genre'),
    path('genre/?sort=<sort>', views.all_genre, name='all_genre'),
    path('genre/<slug:slug_genre>/', views.genre, name='genre'),
    path('album/', views.all_album, name='all_album'),
    path('album/?sort=<sort>', views.all_album, name='all_album'),
    path('album/<slug:slug_album>/', views.album, name='album'),
]
