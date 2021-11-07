from django.contrib import admin

from certificate.models import Certificate

# Register your models here.


# Advanced Method
@admin.register(Certificate)

class UserAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'created_date', 'authentication_key')
    search_fields = ('student', 'course', 'created_date')
    #readonly_fields = ('password',)

