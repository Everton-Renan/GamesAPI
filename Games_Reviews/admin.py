from django.contrib import admin

from Games_Reviews import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'reviews', 'release', 'publisher')
    list_display_links = ('id', 'title')


@admin.register(models.GenerateKeys)
class GenerateKeysAdmin(admin.ModelAdmin):
    readonly_fields = ('key', )
