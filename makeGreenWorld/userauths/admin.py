from django.contrib import admin
from userauths.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email','username', 'first_name', 'last_name', 'phone', 'address']
    
admin.site.register(User, UserAdmin)
