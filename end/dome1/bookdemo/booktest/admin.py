from django.contrib import admin

# Register your models here.
from .models import Book, Hero

admin.site.register(Book)
admin.site.register(Hero)
