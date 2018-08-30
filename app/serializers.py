from rest_framework import serializers

from app.models import Movie, Tv, Shows, Animation, Fuli, TvList, ShowList, AnimationList


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_img', 'movie_name', 'director', 'staring', 'movie_type', 'area', 'languages', 'release_time',
                  'update_time', 'summary', 'play_url']


class TvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tv
        fields = ['tv_img', 'tv_name', 'director', 'staring', 'tv_type', 'area', 'languages', 'release_time',
                  'update_time', 'summary']


class ShowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shows
        fields = ['show_img', 'show_name', 'director', 'staring', 'show_type', 'area', 'languages', 'release_time',
                  'update_time', 'summary']


class AnimationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animation
        fields = ['animation_img', 'animation_name', 'director', 'staring', 'animation_type', 'area', 'languages',
                  'release_time', 'update_time', 'summary', 'play_url']


class FuliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuli
        fields = ['fuli_img', 'fuli_name', 'director', 'staring', 'fuli_type', 'area', 'languages', 'release_time',
                  'update_time', 'summary', 'play_url']


class TvListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TvList
        fields = ['tv_name', 'num', 'play_url']


class ShowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowList
        fields = ['show_name', 'num', 'play_url']


class AnimationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimationList
        fields = ['animation_name', 'num', 'play_url']
