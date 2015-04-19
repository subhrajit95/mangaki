# coding=utf8
from mangaki.models import Anime, Manga, Genre, Track, OST, Artist, Rating, Page, Suggestion, SearchIssue
from django.contrib import admin


class AnimeAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title')
    list_display = ('id', 'title', 'nsfw')
    list_filter = ('nsfw',)


class MangaAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title')
    list_display = ('id', 'title', 'nsfw')
    list_filter = ('nsfw',)


class GenreAdmin(admin.ModelAdmin):
    pass


class TrackAdmin(admin.ModelAdmin):
    pass


class OSTAdmin(admin.ModelAdmin):
    pass


class ArtistAdmin(admin.ModelAdmin):
    pass


class RatingAdmin(admin.ModelAdmin):
    pass


class PageAdmin(admin.ModelAdmin):
    pass


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('work', 'problem', 'date', 'user', 'is_checked')
    list_filter = ('problem',)


class SearchIssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user')


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Manga, MangaAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(OST, OSTAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(SearchIssue, SearchIssueAdmin)
