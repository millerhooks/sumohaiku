from django.contrib import admin

from stats.models import Stat, Asset

admin.site.register(Asset)
admin.site.register(Stat)