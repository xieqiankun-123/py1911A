from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


class OptionInline(admin.StackedInline):
    model = Options
    extra = 1


# Register your models here.
class VoteAdmin(ModelAdmin):
    list_display = ("id", "title")
    inlines = [OptionInline]


class OptionsAdmin(ModelAdmin):
    list_display = ("id", "opt_title", "opt_poll", "opt_vote")


admin.site.register(User)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Options, OptionsAdmin)
