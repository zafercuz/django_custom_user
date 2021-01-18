# Generated by Django 3.0.11 on 2021-01-18 06:30

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('TID', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='table id')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('Emp_ID', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=10, unique=True, verbose_name='employee id')),
                ('username', models.CharField(db_column='Username', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=50, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('password', models.CharField(db_column='myPassword', max_length=128, verbose_name='password')),
                ('FName', models.CharField(blank=True, max_length=50, null=True, verbose_name='first name')),
                ('MI', models.CharField(blank=True, max_length=50, null=True, verbose_name='middle initial')),
                ('LName', models.CharField(blank=True, max_length=50, null=True, verbose_name='last name')),
                ('Designation', models.CharField(blank=True, max_length=50, null=True, verbose_name='designation')),
                ('Office', models.CharField(blank=True, max_length=50, null=True, verbose_name='office')),
                ('Department', models.CharField(blank=True, max_length=50, null=True, verbose_name='department')),
                ('BranchCode', models.CharField(max_length=10, verbose_name='branch code')),
                ('email', models.EmailField(db_column='Email_Address', max_length=50, unique=True, verbose_name='email')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates whether this user should be treated as a superuser.', verbose_name='superuser status')),
                ('is_admin', models.BooleanField(db_column='Is_Admin', default=False, help_text='Designates whether this user should be treated as an admin.', verbose_name='admin status')),
                ('is_hr', models.BooleanField(db_column='Is_HR', default=False, help_text='Designates whether this user should be treated as a HR.', verbose_name='hr status')),
                ('is_LMS', models.BooleanField(db_column='Is_LMS', default=False, help_text='Designates whether this user should be treated as a lms.', verbose_name='lms status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('IPAdd_Login', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip address login')),
                ('IsOnline', models.BooleanField(default=False, help_text='Designates whether the user is online.', verbose_name='is online')),
                ('Machine', models.CharField(blank=True, max_length=20, null=True)),
                ('Product_Version', models.CharField(blank=True, max_length=20, null=True)),
                ('is_approver', models.BooleanField(db_column='is_approver', default=True, help_text='Designates whether this user should be treated as an approver.', verbose_name='approver')),
                ('Company', models.CharField(blank=True, max_length=100, null=True)),
                ('is_inquiry', models.BooleanField(db_column='Is_Inquiry', default=True, help_text='Designates whether this user should be treated as an inquiry.', verbose_name='inquiry')),
                ('TransactedBy', models.CharField(blank=True, max_length=50, null=True)),
                ('PostingDate', models.DateTimeField(blank=True, null=True, verbose_name='posting date')),
                ('Reset_Pass', models.BooleanField(blank=True, default=False, null=True)),
                ('UFullName', models.CharField(blank=True, max_length=100, null=True)),
                ('BranchName', models.CharField(blank=True, max_length=50, null=True)),
                ('CCode', models.CharField(blank=True, max_length=10, null=True)),
                ('Is_UniformMgmt', models.BooleanField(blank=True, default=False, null=True)),
                ('Is_Insurance', models.BooleanField(blank=True, default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'UserManagement',
            },
        ),
    ]
