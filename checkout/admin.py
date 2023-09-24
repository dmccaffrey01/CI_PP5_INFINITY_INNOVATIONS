from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'real_items_total', 'discounted_total',
                       'grand_total',)
    
    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'discounted_total',
              'real_items_total', 'grand_total',)
    
    ordering = ('-date',)

    inlines = [OrderLineItemAdmin]


admin.site.register(Order, OrderAdmin)