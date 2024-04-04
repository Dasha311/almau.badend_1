from django.db import models

# Create your models here.
class Moves(models.Model):
    titel = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=300, default='')
    producer = models.CharField(null=False, max_length=300, default='')
    duration = models.IntegerField(null=False, default=0)

    def __str__(self):
        return f'ID: {self.id} {self.name}'
