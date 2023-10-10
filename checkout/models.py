import uuid
from decimal import Decimal

from django.db import models
from django.db.models import Sum
from django.conf import settings
from datetime import timedelta

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     blank=True, null=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254,  null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    real_items_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    discounted_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default="")

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs and discount
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total > settings.DISCOUNT_THRESHOLD:
            self.discounted_total = self.order_total - (Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100) * self.order_total)
        else:
            self.discounted_total = self.order_total
        
        if self.real_items_total > 0:
            self.delivery_cost = Decimal(settings.STANDARD_DELIVERY_COST)
        else:
            self.delivery_cost = 0

        self.grand_total = self.discounted_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
            """
            Override the original save method to set the order number
            if it hasn't been set already
            """
            if not self.order_number:
                self.order_number = self._generate_order_number()
            super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_theme = models.CharField(max_length=10, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to save the lineitem total
        and update the order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'


class TrackingOrder(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='trackingOrder')
    tracking_number = models.CharField(max_length=64, null=False, editable=False)
    status = models.CharField(max_length=32, null=False, blank=False, default="On Route")
    location = models.CharField(max_length=32, null=False, blank=False, default="Mockville, MO")
    estimated_delivery = models.DateTimeField()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the tracking number
        estimated delivery
        if it hasn't been set already
        """
        if not self.tracking_number:
            self.tracking_number = f'tn_{self.order.order_number}'
            self.estimated_delivery = self.order.date + timedelta(days=5)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.tracking_number

    
