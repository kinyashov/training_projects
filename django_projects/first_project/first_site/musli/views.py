from django.shortcuts import render

from .models import Track, Performer, Album, Genre


def index(request):
    list_of_performers = Performer.objects.all()[:10]
    list_of_albums = Album.objects.all()[:10]
    list_of_genres = Genre.objects.all()[:10]
    context = {'list_of_performers': list_of_performers,
               'list_of_albums': list_of_albums,
               'list_of_genres': list_of_genres}
    return render(request, 'musli/index.html', context=context)


def all_performer(request):
    list_of_performers = Performer.objects.all()
    context = {'list_of_performers': list_of_performers}
    return render(request, 'musli/all_performer.html', context=context)


def performer(request, slug_performer):
    performer = Performer.objects.get(slug=slug_performer)
    list_of_tracks = Track.objects.filter(performer_id=performer.id)
    albums = Album.objects.filter(performer_id=performer.id)
    genres = Genre.objects.filter(performer=performer)
    context = {'performer': performer,
               'list_of_tracks': list_of_tracks,
               'genres': genres,
               'albums': albums}
    return render(request, 'musli/performer.html', context=context)


def all_genre(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return render(request, 'musli/all_genre.html', context=context)


def genre(request, slug_genre):
    genre = Genre.objects.get(slug=slug_genre)
    performers = Performer.objects.filter(genre=genre)
    albums = Album.objects.filter(genre=genre)
    tracks = Track.objects.filter(genre=genre)
    context = {'genre': genre,
               'performers': performers,
               'albums': albums,
               'tracks': tracks}
    return render(request, 'musli/genre.html', context=context)


def all_album(request):
    list_of_albums = Album.objects.all()
    context = {'list_of_albums': list_of_albums}
    return render(request, 'musli/all_album.html', context=context)


def album(request, slug_album):
    album = Album.objects.get(slug=slug_album)
    list_of_tracks = Track.objects.filter(album_id=album.id)
    genres = Genre.objects.filter(album=album)
    performer = Performer.objects.get(album=album)
    context = {'album': album,
               'list_of_tracks': list_of_tracks,
               'genres': genres,
               'performer': performer}
    return render(request, 'musli/album.html', context=context)
