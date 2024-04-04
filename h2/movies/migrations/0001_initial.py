# Generated by Django 5.0.2 on 2024-02-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(default='', max_length=255)),
                ('description', models.CharField(default='', max_length=300)),
                ('producer', models.CharField(default='', max_length=300)),
                ('duration', models.IntegerField(default=0)),
            ],
        ),
    ]
