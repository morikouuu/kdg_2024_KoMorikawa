from django.contrib import admin
from .models import Blog,Comment,Reply,Likes
# Register your models here.



admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Likes)
