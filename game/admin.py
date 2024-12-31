from django.contrib import admin
from django.utils.html import format_html
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_preview' , 'name', 'slug', 'created_at', 'updated_at', 'visit_game_link')
    readonly_fields = ('thumbnail_preview', 'visit_game_link')
    prepopulated_fields = {'slug': ('name',)}

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px; border-radius:10px;" />', obj.thumbnail)
        return "No Thumbnail"

    thumbnail_preview.short_description = "Thumbnail Preview"

    def visit_game_link(self, obj):
        return format_html('<a href="/game/{}/" target="_blank">Visit Game</a>', obj.slug)

    visit_game_link.short_description = "Visit Game"

admin.site.register(Game, GameAdmin)
