# Generated by Django 3.0.11 on 2021-01-26 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210126_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_approver',
            field=models.BooleanField(db_column='is_approver', default=False, help_text='Designates whether this user should be treated as an approver.', verbose_name='approver'),
        ),
    ]
