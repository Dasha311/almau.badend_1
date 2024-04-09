from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(null=False, max_length=255, default='')
    description = models.CharField(null=False, max_length=2000, default='')
    due_date = models.DateField(null=False, max_length=255, default='')
    status = models.BooleanField(null=False, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f'ID: {self.id} {self.title}'

class BasketItem(models.Model):
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False, default=1)

    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'

    def __str__(self):
        return f'ID: {self.id} {self.owner} {self.todo.title} {self.amount}'
