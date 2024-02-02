from django.contrib import admin
from .models import Client, Good, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'address', 'date_of_registration']
    list_editable = ['email', 'phone_number', 'address', ]
    list_filter = ['date_of_registration']
    search_fields = ['name', 'email', 'phone_number', 'address']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'total_price']



@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'count', 'image']
    list_editable = ['description', 'price', 'count', 'image']
    search_fields = ['name', 'description', 'price', 'count']
    actions = [reset_quantity]
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['description'],

            },
        ), (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            })
        , ]