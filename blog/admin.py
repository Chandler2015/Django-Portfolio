from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):

    list_display = ['title', 'summary', 'pub_date_pretty', 'is_published']


admin.site.register(Blog, BlogAdmin)
