from django.contrib import admin
from .models import Blog,comments

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog','id')

class commentsAdmin(admin.ModelAdmin):
    list_display = ('parent','user','related_blog','text','id')

admin.site.register(Blog,BlogAdmin)
admin.site.register(comments,commentsAdmin)