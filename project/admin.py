from django.contrib import admin
from .models import Project
from django.db import models


class ProjectAdmin(admin.ModelAdmin):

    list_display = ['title', 'image', 'summary', 'link', 'pub_date']


admin.site.register(Project, ProjectAdmin)
