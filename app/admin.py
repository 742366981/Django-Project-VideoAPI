from django.contrib import admin

from app.models import Movie, Tv, TvList, Shows, ShowList, AnimationList, Animation, Fuli


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'movie_img', 'director', 'staring', 'movie_type', 'area', 'languages', 'release_time',
                    'update_time', 'play_url']
    search_fields = ['movie_name', 'movie_type', 'release_time']
    ordering = ['-release_time']


admin.site.register(Movie, MovieAdmin)


class TvAdmin(admin.ModelAdmin):
    list_display = ['tv_name', 'tv_img', 'director', 'staring', 'tv_type', 'area', 'languages', 'release_time',
                    'update_time']
    search_fields = ['tv_name', 'tv_type', 'release_time']
    ordering = ['-release_time']


admin.site.register(Tv, TvAdmin)


class TvListAdmin(admin.ModelAdmin):
    list_display = ['tv_name', 'num', 'play_url']
    search_fields = ['tv_name']


admin.site.register(TvList, TvListAdmin)


class ShowsAdmin(admin.ModelAdmin):
    list_display = ['show_name', 'show_img', 'director', 'staring', 'show_type', 'area', 'languages', 'release_time',
                    'update_time']
    search_fields = ['show_name', 'show_type', 'release_time']
    ordering = ['-release_time']


admin.site.register(Shows, ShowsAdmin)


class ShowListAdmin(admin.ModelAdmin):
    list_display = ['show_name', 'num', 'play_url']
    search_fields = ['show_name']


admin.site.register(ShowList, ShowListAdmin)


class AnimationAdmin(admin.ModelAdmin):
    list_display = ['animation_name', 'animation_img', 'director', 'staring', 'animation_type', 'area', 'languages',
                    'release_time', 'update_time']
    search_fields = ['animation_name', 'animation_type', 'release_time']
    ordering = ['-release_time']


admin.site.register(Animation, AnimationAdmin)


class AnimationListAdmin(admin.ModelAdmin):
    list_display = ['animation_name', 'num', 'play_url']
    search_fields = ['animation_name']


admin.site.register(AnimationList, AnimationListAdmin)


class FuliAdmin(admin.ModelAdmin):
    list_display = ['fuli_name', 'fuli_img', 'director', 'staring', 'fuli_type', 'area', 'languages', 'release_time',
                    'update_time', 'play_url']
    search_fields = ['movie_name', 'movie_type', 'release_time']
    ordering = ['-release_time']


admin.site.register(Fuli, FuliAdmin)
