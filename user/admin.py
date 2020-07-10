from django.contrib import admin

from .models import UserDetails, Email, Mobile

admin.site.register(UserDetails)
admin.site.register(Email)
admin.site.register(Mobile)
