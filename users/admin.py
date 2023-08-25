from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'role')  # Fields to display in the list view
    list_filter = ('role',)  # Fields for filtering
    search_fields = ('name', 'email')  # Fields for searching

admin.site.register(User, UserAdmin)
 