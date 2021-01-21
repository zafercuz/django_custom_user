# Generated by Django 3.0.11 on 2021-01-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_marketing',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as marketing team.', verbose_name='marketing'),
        ),
    ]
