from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(null=False, max_length=255, blank=False)
    description = models.CharField(null=False, max_length=2000, blank=True, default='')
    duration = models.PositiveIntegerField(null=False)
    producer = models.CharField(null=False, max_length=255)
    created_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'ID: {self.id} {self.title}'

class CartItem(models.Model):
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='movies_cart_items')
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, default=1)

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'

    def __str__(self):
        return f'ID: {self.id} {self.owner} {self.movies.title} {self.amount}'
