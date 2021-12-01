from django.contrib import admin

from artwork.models import Entry, Comment


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "published", "picture")
    list_display_links = ("title",)


@admin.register(Comment)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "entry", "text")
    list_display_links = ("entry",)
