from django.contrib import admin

from app.models import Movie, Tv, TvList, Shows, ShowList, AnimationList, Animation, Fuli


# 修改网页title
admin.site.site_title = 'API数据后台管理'
# 修改网页header
admin.site.site_header = 'API数据后台管理'


class MovieAdmin(admin.ModelAdmin):
    # list_display设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ['movie_name', 'movie_img', 'director', 'staring', 'movie_type', 'area', 'languages', 'release_time',
                    'update_time', 'play_url']
    # 搜索功能及能实现搜索的字段
    search_fields = ['movie_name', 'movie_type', 'release_time']
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ['-release_time']
    # list_per_page设置每页显示多少条记录，默认是100条
    # list_per_page = 100
    # 操作项功能显示位置设置，两个都为True则顶部和底部都显示
    actions_on_top = True
    actions_on_bottom = True
    # 操作项功能显示选中项的数目
    # actions_selection_counter = True
    # 字段为空值显示的内容
    empty_value_display = ' -空白- '
    # list_editable 设置默认可编辑字段（第一个默认不可编辑，因为它是一个链接，点击会进入修改页面）
    list_editable = ['play_url']
    # 过滤器功能及能过滤的字段
    list_filter = ['movie_type', 'languages', 'release_time']


admin.site.register(Movie, MovieAdmin)


class TvAdmin(admin.ModelAdmin):
    list_display = ['tv_name', 'tv_img', 'director', 'staring', 'tv_type', 'area', 'languages', 'release_time',
                    'update_time']
    search_fields = ['tv_name', 'tv_type', 'release_time']
    ordering = ['-release_time']
    actions_on_top = True
    actions_on_bottom = True
    empty_value_display = ' -空白- '
    list_filter = ['tv_type', 'languages', 'release_time']


admin.site.register(Tv, TvAdmin)


class TvListAdmin(admin.ModelAdmin):
    list_display = ['tv_name', 'num', 'play_url']
    search_fields = ['tv_name__tv_name']
    empty_value_display = ' -空白- '
    list_editable = ['play_url']


admin.site.register(TvList, TvListAdmin)


class ShowsAdmin(admin.ModelAdmin):
    list_display = ['show_name', 'show_img', 'director', 'staring', 'show_type', 'area', 'languages', 'release_time',
                    'update_time']
    search_fields = ['show_name', 'show_type', 'release_time']
    ordering = ['-release_time']
    actions_on_top = True
    actions_on_bottom = True
    empty_value_display = ' -空白- '
    list_filter = ['show_type', 'languages', 'release_time']


admin.site.register(Shows, ShowsAdmin)


class ShowListAdmin(admin.ModelAdmin):
    list_display = ['show_name', 'num', 'play_url']
    search_fields = ['show_name__show_name']
    empty_value_display = ' -空白- '
    list_editable = ['play_url']


admin.site.register(ShowList, ShowListAdmin)


class AnimationAdmin(admin.ModelAdmin):
    list_display = ['animation_name', 'animation_img', 'director', 'staring', 'animation_type', 'area', 'languages',
                    'release_time', 'update_time']
    search_fields = ['animation_name', 'animation_type', 'release_time']
    ordering = ['-release_time']
    actions_on_top = True
    actions_on_bottom = True
    empty_value_display = ' -空白- '
    list_filter = ['animation_type', 'languages', 'release_time']


admin.site.register(Animation, AnimationAdmin)


class AnimationListAdmin(admin.ModelAdmin):
    list_display = ['animation_name', 'num', 'play_url']
    search_fields = ['animation_name__animation_name']
    empty_value_display = ' -空白- '
    list_editable = ['play_url']


admin.site.register(AnimationList, AnimationListAdmin)


class FuliAdmin(admin.ModelAdmin):
    list_display = ['fuli_name', 'fuli_img', 'director', 'staring', 'fuli_type', 'area', 'languages', 'release_time',
                    'update_time', 'play_url']
    search_fields = ['movie_name', 'movie_type', 'release_time']
    ordering = ['-release_time']
    actions_on_top = True
    actions_on_bottom = True
    empty_value_display = ' -空白- '
    list_editable = ['play_url']
    list_filter = ['fuli_type', 'languages', 'release_time']


admin.site.register(Fuli, FuliAdmin)
