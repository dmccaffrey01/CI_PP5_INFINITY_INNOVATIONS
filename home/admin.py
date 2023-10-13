from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Review admin class
    """
    list_display = (
        'id',
        'message',
    )

admin.site.register(Review, ReviewAdmin)