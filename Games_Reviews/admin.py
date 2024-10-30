from django.contrib import admin

from Games_Reviews import models


class GenreInLine(admin.TabularInline):
    model = models.Genre
    extra = 1


class ModeInLine(admin.TabularInline):
    model = models.Mode
    extra = 1


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'reviews', 'release', 'publisher')
    inlines = GenreInLine, ModeInLine
