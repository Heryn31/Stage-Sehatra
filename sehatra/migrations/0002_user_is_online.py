# Generated by Django 5.1.1 on 2024-11-27 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sehatra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]