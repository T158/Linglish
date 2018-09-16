from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    number = models.CharField('番号', max_length=20)
    word = models.CharField('単語', max_length=100)
    meaning = models.CharField('意味', max_length=100)
    example = models.CharField('例文', max_length=500)

    def __str__(self):
        return self.name


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return 'wish list - {}'.format(self.user.username)