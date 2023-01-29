from django.contrib import admin

from .models import Article, Tag, Scope

#
# class RelationshipInline(admin.TabularInline):
#     model = Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    list_filter = ['title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
