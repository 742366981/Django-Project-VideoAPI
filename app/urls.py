from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from app import views

movie_router = SimpleRouter()
movie_router.register('movies', views.MovieSource)
tv_router = SimpleRouter()
tv_router.register('tv', views.TvSource)
shows_router = SimpleRouter()
shows_router.register('shows', views.ShowsSource)
animation_router = SimpleRouter()
animation_router.register('animation', views.AnimationSource)
fuli_router = SimpleRouter()
fuli_router.register('fuli', views.FuliSource)
urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'register/', views.register, name='register'),
    url(r'login/', views.login, name='login'),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^tvList/', views.TvListView.as_view()),
]
urlpatterns += movie_router.urls + tv_router.urls + shows_router.urls + animation_router.urls + fuli_router.urls
