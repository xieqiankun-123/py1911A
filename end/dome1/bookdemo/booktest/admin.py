from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.
from .models import Book, Hero


class HeroInline(admin.StackedInline):
    model = Hero
    extra = 1


class BookAdmin(ModelAdmin):
    list_display = ('id', 'title', 'price')
    search_fields = ['title', 'id']
    list_per_page = 5
    list_filter = ('title', 'price')
    inlines = [HeroInline]


class HeroAdmin(ModelAdmin):
    list_display = ('id', 'name', 'gender', 'content', 'book')
    search_fields = ['name', 'gender']
    list_filter = ('book', 'gender')


admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
