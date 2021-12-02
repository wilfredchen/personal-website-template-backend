from django.contrib import admin

# Register your models here.

from .models import UISetting, User

admin.site.register(User)
admin.site.register(UISetting)