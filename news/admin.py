from django.contrib import admin

from news.models import Event, NewsCategory

@admin.register(NewsCategory)
class NewsCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


