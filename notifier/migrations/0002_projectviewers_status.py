# Generated by Django 4.0.3 on 2022-03-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectviewers',
            name='status',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]