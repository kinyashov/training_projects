from django.db import models


class Performer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default=None, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    genre = models.ManyToManyField('Genre')

    class Meta:
        verbose_name = 'Испольнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default=None, blank=True, null=True)
    performer = models.ForeignKey('Performer', on_delete=models.DO_NOTHING)
    partner = models.ManyToManyField('Performer', related_name='album_partners', blank=True)
    genre = models.ManyToManyField('Genre')
    realised = models.DateField()
    added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        name = '{} - {}'.format(self.performer, self.title)
        return name


class Genre(models.Model):
    genre = models.CharField(max_length=255)
    description = models.TextField(default=None, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.genre


class Track(models.Model):
    title = models.CharField(max_length=255)
    performer = models.ForeignKey('Performer', related_name='tracks_by_performer', on_delete=models.DO_NOTHING)
    partner = models.ManyToManyField('Performer', related_name='track_partners', blank=True)
    genre = models.ManyToManyField('Genre', related_name='tracks', default=None, blank=True)
    album = models.ForeignKey('Album', blank=True, null=True, on_delete=models.DO_NOTHING)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Трек'
        verbose_name_plural = 'Треки'

    def __str__(self):
        name = '{} - {}'.format(self.performer, self.title)
        return name
