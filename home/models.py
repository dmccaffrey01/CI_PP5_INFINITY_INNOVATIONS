from django.db import models


class Review(models.Model):
    """ Review model """
    message = models.TextField()

    def __str__(self):
        return f'Message: {self.id}'
