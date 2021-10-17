from django.contrib import admin
from .models import Student

# Register your models here.

# Simple Method
#admin.site.register(Student)

# Advanced Method
@admin.register(Student)

class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'password')
    search_fields = ('firstname', 'lastname', 'email')
    readonly_fields = ('password',)
