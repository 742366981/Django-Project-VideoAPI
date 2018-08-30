from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# 电影
class Movie(models.Model):
    movie_img = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=50, unique=True)
    director = models.CharField(max_length=50)
    staring = models.CharField(max_length=200)
    movie_type = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    languages = models.CharField(max_length=30)
    release_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=30)
    summary = models.CharField(max_length=2000)
    play_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'movie'


# 电视剧
class Tv(models.Model):
    tv_img = models.CharField(max_length=255)
    tv_name = models.CharField(max_length=50, primary_key=True, unique=True)
    director = models.CharField(max_length=50)
    staring = models.CharField(max_length=200)
    tv_type = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    languages = models.CharField(max_length=30)
    release_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=30)
    summary = models.CharField(max_length=2000)

    class Meta:
        db_table = 'tv'


# 综艺
class Shows(models.Model):
    show_img = models.CharField(max_length=255)
    show_name = models.CharField(max_length=50, primary_key=True, unique=True)
    director = models.CharField(max_length=50)
    staring = models.CharField(max_length=200)
    show_type = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    languages = models.CharField(max_length=30)
    release_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=30)
    summary = models.CharField(max_length=2000)

    class Meta:
        db_table = 'shows'


# 动漫
class Animation(models.Model):
    animation_img = models.CharField(max_length=255)
    animation_name = models.CharField(max_length=50, primary_key=True, unique=True)
    director = models.CharField(max_length=50)
    staring = models.CharField(max_length=200)
    animation_type = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    languages = models.CharField(max_length=30)
    release_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=30)
    summary = models.CharField(max_length=2000)

    class Meta:
        db_table = 'animation'


# 福利
class Fuli(models.Model):
    movie_img = models.CharField(max_length=255)
    movie_name = models.CharField(max_length=50, unique=True)
    director = models.CharField(max_length=50)
    staring = models.CharField(max_length=200)
    movie_type = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    languages = models.CharField(max_length=30)
    release_time = models.CharField(max_length=50)
    update_time = models.CharField(max_length=30)
    summary = models.CharField(max_length=2000)
    play_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'fuli'


# 电视剧集数
class TvList(models.Model):
    tv_name = models.ForeignKey(Tv, db_column='tv_name')
    num = models.CharField(max_length=30)
    play_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'tv_list'


# 综艺期数
class ShowList(models.Model):
    show_name = models.ForeignKey(Shows, db_column='tv_name')
    num = models.CharField(max_length=30)
    play_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'show_list'


# 动漫集数
class AnimationList(models.Model):
    animation_name = models.ForeignKey(Animation, db_column='tv_name')
    num = models.CharField(max_length=30)
    play_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'animation_list'
