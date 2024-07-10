from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('nickname','username','first_name','last_name','email','is_staff')
    list_filter = ('username','first_name','last_name','is_staff')
    search_fields = ('username','first_name','last_name','is_staff')

admin.site.register(User,UserAdmin)



