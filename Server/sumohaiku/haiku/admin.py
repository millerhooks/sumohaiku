from django.contrib import admin

from haiku.models import UserProfile, Haiku

admin.site.register(UserProfile)
admin.site.register(Haiku)