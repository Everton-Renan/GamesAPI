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
    list_display_links = ('id', 'title')
    inlines = GenreInLine, ModeInLine


@admin.register(models.NewUser)
class NewUserAdmin(admin.ModelAdmin):
    readonly_fields = ('key', )
    fields = [
        'first_name',
        'last_name',
        'username',
        'email',
        'password',
        'is_staff',
        'is_superuser',
        'is_active',
        'date_joined',
        'last_login',
        'groups',
        'user_permissions',
        'key'
    ]
    list_display = ('id', 'first_name', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name')
