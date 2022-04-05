# Generated by Django 4.0.3 on 2022-03-23 06:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0002_projectviewers_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectviewers',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
