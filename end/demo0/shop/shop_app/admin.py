from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(GoodCategory)
admin.site.register(Good)
admin.site.register(Ads)
