"""Module for the django administration of general"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .forms import MyUserCreationForm, MyUserChangeForm

from .models import Property, Bid


class UserAdmin(BaseUserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm  # Use the custom change form
    model = get_user_model()
    list_display = ['email', 'first_name', 'surname', 'is_staff', 'is_active']
    list_filter = ['email', 'first_name', 'surname', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('first_name', 'surname', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Viewable Properties', {'fields': ('viewable_properties',)}),  # Add this line
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'surname', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'viewable_properties')}
        ),
    )
    search_fields = ('first_name', 'surname', 'email',)
    ordering = ('first_name', 'surname', 'email',)


admin.site.register(Property)
admin.site.register(Bid)
admin.site.register(get_user_model(), UserAdmin)