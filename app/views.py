from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import mixins, viewsets, filters
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from app.filters import MovieFilter
from app.models import Movie, Tv, Shows, Animation, Fuli, TvList, ShowList, AnimationList
from app.serializers import MovieSerializer, TvSerializer, ShowsSerializer, AnimationSerializer, FuliSerializer, \
    TvListSerializer, ShowListSerializer, AnimationListSerializer


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return HttpResponseRedirect(reverse('video:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('video:index'))


def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        pages = []
        n = 1
        for _ in movies[::10]:
            pages.append(n)
            n += 1
        return render(request, 'index.html', {'pages': pages})


class MovieSource(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # 使用搜索功能后，过滤失效，可以注释掉相关代码
    # filter_class = MovieFilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('movie_name', 'movie_type')


class TvSource(mixins.ListModelMixin,
               viewsets.GenericViewSet):
    queryset = Tv.objects.all()
    serializer_class = TvSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('tv_name', 'tv_type')


class ShowsSource(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Shows.objects.all()
    serializer_class = ShowsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('show_name', 'show_type')


class AnimationSource(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Animation.objects.all()
    serializer_class = AnimationSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('animation_name', 'animation_type')


class FuliSource(mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = Fuli.objects.all()
    serializer_class = FuliSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('fuli_name', 'fuli_type')


class MyPageNumberPagination(PageNumberPagination):
    # 每页显示多少个
    page_size = 100
    # 默认每页显示3个，可以通过url传入?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    # 最大页数不超过10
    max_page_size = 10
    # 获取页码数的
    page_query_param = "page"


class TvListView(mixins.ListModelMixin,
                 GenericAPIView):

    def get(self, request, *args, **kwargs):
        # 自定义一个电视剧name参数
        name = request.GET.get('name')
        if name:
            tv_list = TvList.objects.filter(tv_name=name)
        else:
            # 获取所有数据
            tv_list = TvList.objects.all()
        # 创建分页对象，这里是自定义的MyPageNumberPagination
        page = MyPageNumberPagination()
        # 获取分页的数据
        tv_list_page = page.paginate_queryset(queryset=tv_list, request=request, view=self)
        # 对数据进行序列化
        ser = TvListSerializer(instance=tv_list_page, many=True)
        # return Response(ser.data)  # 不含上一页下一页
        return page.get_paginated_response(ser.data)


class ShowListView(mixins.ListModelMixin,
                   GenericAPIView):

    def get(self, request, *args, **kwargs):
        # 自定义一个电视剧name参数
        name = request.GET.get('name')
        if name:
            tv_list = TvList.objects.filter(tv_name=name)
        else:
            # 获取所有数据
            tv_list = TvList.objects.all()
        # 创建分页对象，这里是自定义的MyPageNumberPagination
        page = MyPageNumberPagination()
        # 获取分页的数据
        tv_list_page = page.paginate_queryset(queryset=tv_list, request=request, view=self)
        # 对数据进行序列化
        ser = TvListSerializer(instance=tv_list_page, many=True)
        # return Response(ser.data)  # 不含上一页下一页
        return page.get_paginated_response(ser.data)
