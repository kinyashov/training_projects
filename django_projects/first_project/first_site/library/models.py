from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Genre(models.Model):
    genre = models.CharField(max_length=30)
    description = models.TextField(default=None)

    def __str__(self):
        return self.genre


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.OneToOneField('Author', on_delete=models.DO_NOTHING, default=None)
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return self.title
