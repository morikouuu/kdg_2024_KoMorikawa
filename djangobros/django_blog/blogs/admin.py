from django.contrib import admin
from .models import Blog,Comment,Reply
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_datetime', 'updated_datetime')
    list_display_links = ('id', 'title')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Reply)
