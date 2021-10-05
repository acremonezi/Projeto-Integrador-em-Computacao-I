from django.contrib import admin
from .models import User

# Register your models here.

# Cadastra o app user na área administrativa do django

from .models import User

#admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'password')
    search_fields = ('firstname', 'lastname', 'email')
    readonly_fields = ('password',)