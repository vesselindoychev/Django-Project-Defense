from django.contrib import admin

from registration.accounts.models import RegistrationUser, Profile


@admin.register(RegistrationUser)
class RegistrationUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',)