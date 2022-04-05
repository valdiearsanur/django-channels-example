from django.contrib import admin

from .models import ProjectViewers


@admin.register(ProjectViewers)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'status', 'timestamp']
