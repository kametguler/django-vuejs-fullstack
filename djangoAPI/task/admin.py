from django.contrib import admin
from .models import *


class TaskAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
    list_display = ['title', 'description', 'created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
