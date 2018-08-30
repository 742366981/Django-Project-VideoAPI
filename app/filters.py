import django_filters
from rest_framework import filters

from app.models import Movie, TvList


class MovieFilter(filters.FilterSet):
    name = django_filters.CharFilter('movie_name', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['movie_name']


class TvListFilter(filters.FilterSet):
    name = django_filters.CharFilter('tv_name', lookup_expr='icontains')

    class Meta:
        model = TvList
        fields = ['tv_name']

