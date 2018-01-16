from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.nickname


class Twit(models.Model):
    twit = models.TextField(max_length=280)
    author = models.OneToOneField('User', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Твит'
        verbose_name_plural = 'Твиты'


class Like(models.Model):
    twit_liked = models.OneToOneField('Twit', on_delete=models.DO_NOTHING)
    user_liked = models.OneToOneField('User', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Reply(models.Model):
    text = models.TextField()
    twit = models.OneToOneField('Twit', on_delete=models.DO_NOTHING)
    author = models.OneToOneField('User', on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
