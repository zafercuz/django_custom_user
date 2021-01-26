# Generated by Django 3.0.11 on 2021-01-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_is_marketing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='FName',
            field=models.CharField(max_length=50, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='LName',
            field=models.CharField(max_length=50, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='MI',
            field=models.CharField(max_length=50, null=True, verbose_name='middle initial'),
        ),
    ]