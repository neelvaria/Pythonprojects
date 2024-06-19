from django.contrib import admin
from .models import *

# Register your models here.
class urls(admin.ModelAdmin):
    list_display = ('link','uuid')
admin.site.register(url,urls)