from django.contrib import admin

# Register your models here.

from .models import UISetting,User,Blog

admin.site.register(User)
admin.site.register(UISetting)
admin.site.register(Blog)