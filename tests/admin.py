# taxi/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    """Admin for Driver (custom user)."""
    # покажемо license_number в списку
    list_display = ('username', 'email', 'first_name', 'last_name', 'license_number', 'is_staff')

    # полe, що буде доступне для пошуку
    search_fields = ('username', 'first_name', 'last_name', 'email', 'license_number')

    # додаємо license_number в секцію "Additional info" у розділі fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional info'), {'fields': ('license_number',)}),
    )

    # додаємо license_number також у формі додавання користувача
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional info'), {
            'classes': ('wide',),
            'fields': ('license_number',),
        }),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    search_fields = ('model',)  # зробити можливість шукати Car по model
    list_filter = ('manufacturer',)  # фільтр за manufacturer
