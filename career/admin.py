from django.contrib import admin

from CustomUser.admin_no_log import DontLog
from .models import Career


class CareerModelAdmin(DontLog, admin.ModelAdmin):
    list_display = ('career_name', 'date_posted',)
    list_filter = ('date_posted',)


admin.site.register(Career, CareerModelAdmin)
