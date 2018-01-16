from django.db import models


class Performer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=30)
    performer = models.ForeignKey('Performer', on_delete=models.DO_NOTHING)
    genre = models.ForeignKey('Genre', on_delete=models.DO_NOTHING)
    year = models.PositiveSmallIntegerField(default=None)
    month = models.PositiveSmallIntegerField(default=None)

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.genre


class Track(models.Model):
    title = models.CharField(max_length=30)
    performer = models.OneToOneField('Performer', on_delete=models.DO_NOTHING)
    genre = models.ForeignKey('Genre', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
