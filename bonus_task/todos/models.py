from django.db import models


class Todo(models.Model):
    title = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=2000, default='')
    due_date = models.DateField(null=False, max_length=255, default='')
    status = models.BooleanField(null=False, default=0)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f'ID: {self.id} {self.title}'

