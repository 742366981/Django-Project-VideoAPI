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
    movie_img = models.CharField(max_length=255, verbose_name='图片地址')
    movie_name = models.CharField(max_length=50, unique=True, verbose_name='片名')
    director = models.CharField(max_length=50, verbose_name='导演')
    staring = models.CharField(max_length=200, verbose_name='主演')
    movie_type = models.CharField(max_length=20, verbose_name='类型')
    area = models.CharField(max_length=20, verbose_name='地区')
    languages = models.CharField(max_length=30, verbose_name='语言')
    release_time = models.CharField(max_length=50, verbose_name='上映时间')
    update_time = models.CharField(max_length=30, verbose_name='更新时间')
    summary = models.CharField(max_length=2000, verbose_name='剧情简介')
    play_url = models.CharField(max_length=255, verbose_name='播放地址')

    class Meta:
        db_table = 'movie'
        verbose_name = '电影'
        verbose_name_plural = '电影'


# 电视剧
class Tv(models.Model):
    tv_img = models.CharField(max_length=255, verbose_name='图片地址')
    tv_name = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='剧名')
    director = models.CharField(max_length=50, verbose_name='导演')
    staring = models.CharField(max_length=200, verbose_name='主演')
    tv_type = models.CharField(max_length=20, verbose_name='类型')
    area = models.CharField(max_length=20, verbose_name='地区')
    languages = models.CharField(max_length=30, verbose_name='语言')
    release_time = models.CharField(max_length=50, verbose_name='上映时间')
    update_time = models.CharField(max_length=30, verbose_name='更新时间')
    summary = models.CharField(max_length=2000, verbose_name='剧情简介')

    class Meta:
        db_table = 'tv'
        verbose_name = '电视剧'
        verbose_name_plural = '电视剧'

    def __str__(self):
        return self.tv_name


# 综艺
class Shows(models.Model):
    show_img = models.CharField(max_length=255, verbose_name='图片地址')
    show_name = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='综艺名称')
    director = models.CharField(max_length=50, verbose_name='导演')
    staring = models.CharField(max_length=200, verbose_name='主演')
    show_type = models.CharField(max_length=20, verbose_name='类型')
    area = models.CharField(max_length=20, verbose_name='地区')
    languages = models.CharField(max_length=30, verbose_name='语言')
    release_time = models.CharField(max_length=50, verbose_name='上映时间')
    update_time = models.CharField(max_length=30, verbose_name='更新时间')
    summary = models.CharField(max_length=2000, verbose_name='剧情简介')

    class Meta:
        verbose_name = '综艺'
        verbose_name_plural = '综艺'
        db_table = 'shows'

    def __str__(self):
        return self.show_name


# 动漫
class Animation(models.Model):
    animation_img = models.CharField(max_length=255, verbose_name='图片地址')
    animation_name = models.CharField(max_length=50, primary_key=True, unique=True, verbose_name='动漫名称')
    director = models.CharField(max_length=50, verbose_name='导演')
    staring = models.CharField(max_length=200, verbose_name='主演')
    animation_type = models.CharField(max_length=20, verbose_name='类型')
    area = models.CharField(max_length=20, verbose_name='地区')
    languages = models.CharField(max_length=30, verbose_name='语言')
    release_time = models.CharField(max_length=50, verbose_name='上映时间')
    update_time = models.CharField(max_length=30, verbose_name='更新时间')
    summary = models.CharField(max_length=2000, verbose_name='剧情简介')

    class Meta:
        db_table = 'animation'
        verbose_name = '动漫'
        verbose_name_plural = '动漫'

    def __str__(self):
        return self.animation_name


# 福利
class Fuli(models.Model):
    fuli_img = models.CharField(max_length=255, verbose_name='图片地址')
    fuli_name = models.CharField(max_length=50, unique=True, verbose_name='福利名称')
    director = models.CharField(max_length=50, verbose_name='导演')
    staring = models.CharField(max_length=200, verbose_name='主演')
    fuli_type = models.CharField(max_length=20, verbose_name='类型')
    area = models.CharField(max_length=20, verbose_name='地区')
    languages = models.CharField(max_length=30, verbose_name='语言')
    release_time = models.CharField(max_length=50, verbose_name='上映时间')
    update_time = models.CharField(max_length=30, verbose_name='更新时间')
    summary = models.CharField(max_length=2000, verbose_name='剧情简介')
    play_url = models.CharField(max_length=255, verbose_name='播放地址')

    class Meta:
        db_table = 'fuli'
        verbose_name = '福利'
        verbose_name_plural = '福利'


# 电视剧集数
class TvList(models.Model):
    tv_name = models.ForeignKey(Tv, db_column='tv_name', verbose_name='剧名')
    num = models.CharField(max_length=30, verbose_name='集数')
    play_url = models.CharField(max_length=255, verbose_name='播放地址')

    class Meta:
        db_table = 'tv_list'
        verbose_name = '电视剧集数'
        verbose_name_plural = '电视剧集数'


# 综艺期数
class ShowList(models.Model):
    show_name = models.ForeignKey(Shows, db_column='show_name', verbose_name='综艺名称')
    num = models.CharField(max_length=30, verbose_name='集数')
    play_url = models.CharField(max_length=255, verbose_name='播放地址')

    class Meta:
        db_table = 'show_list'
        verbose_name = '综艺期数'
        verbose_name_plural = '综艺期数'


# 动漫集数
class AnimationList(models.Model):
    animation_name = models.ForeignKey(Animation, db_column='animation_name', verbose_name='动漫名称')
    num = models.CharField(max_length=30, verbose_name='集数')
    play_url = models.CharField(max_length=255, verbose_name='播放地址')

    class Meta:
        db_table = 'animation_list'
        verbose_name = '动漫集数'
        verbose_name_plural = '动漫集数'
