# Generated by Django 5.0.2 on 2024-04-25 02:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_rename_basketitem_cartitem_alter_cartitem_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='todo',
            new_name='movie',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies_cart_items', to=settings.AUTH_USER_MODEL),
        ),
    ]
