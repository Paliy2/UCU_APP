from django.contrib import admin
from events.models import Event

# @admin.action(description='Mark selected events as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.register(Event)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    ordering = ['name']
    actions = [make_published]


