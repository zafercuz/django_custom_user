from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import connections

from CustomUser.admin_no_log import DontLog
from account.forms import UserChangeForm, UserCreationForm
from account.models import Account


class UserDBModelAdmin(DontLog, admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    using = 'other_db'
    # The forms to add and change user instances
    change_form = UserChangeForm
    add_form = UserCreationForm

    def has_add_permission(self, request):
        if not request.user.is_superuser:
            return False
        else:
            return True

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return True

    def has_view_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        else:
            return True

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:
            self.form = self.change_form

        return super().get_form(request, obj, **kwargs)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'Emp_ID', 'is_staff', 'is_admin', 'is_superuser')
    list_filter = ('is_staff', 'is_admin', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('Emp_ID', 'email', 'username',)}),
        ('Permissions',
         {'fields': (
             'is_admin', 'is_active', 'is_staff', 'is_superuser', 'is_hr', 'is_LMS', 'is_approver', 'is_marketing',)}),
        ('Miscellaneous',
         {'fields': (('FName', 'MI', 'LName'), ('BranchCode', 'Designation', 'Office', 'Department'),
                     ('IPAdd_Login', 'Machine'), ('Product_Version', 'Company'),
                     ('IsOnline', 'is_inquiry', 'Is_UniformMgmt', 'Is_Insurance'), ('TransactedBy', 'PostingDate'),
                     'Reset_Pass', ('UFullName', 'BranchName', 'CCode'),)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                ('email', 'username', 'Emp_ID', 'BranchCode',), ('password1', 'password2'), ('FName', 'MI', 'LName')),
        }),
        ('Permissions',
         {'fields': (
             'is_admin', 'is_active', 'is_staff', 'is_superuser', 'is_hr', 'is_LMS', 'is_approver', 'is_marketing')}),
        ('Miscellaneous',
         {'fields': (('Designation', 'Office', 'Department'),
                     ('IPAdd_Login', 'Machine'), ('Product_Version', 'Company'),
                     ('IsOnline', 'is_inquiry', 'Is_UniformMgmt', 'Is_Insurance'), ('TransactedBy', 'PostingDate'),
                     'Reset_Pass', ('UFullName', 'BranchName', 'CCode'),)}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    # Custom Options so that it will point to the second database when adding/editing a new USER
    def save_model(self, request, obj: Account, form, change):
        # Tell Django to save objects to the 'other' database.
        cursor = connections['other_db'].cursor()
        crud_event = "CREATE" if not change else "UPDATE"
        password = form.cleaned_data['password1'] if not change else None
        params = [obj.BranchCode, obj.username, password, obj.FName, obj.MI, obj.LName,
                  obj.Emp_ID, obj.Designation, obj.BranchName, obj.CCode, obj.Company, obj.Office, obj.Department,
                  obj.email, obj.is_approver, obj.is_admin, obj.is_superuser, obj.is_inquiry, obj.is_hr,
                  obj.Is_UniformMgmt, obj.Is_Insurance, obj.TransactedBy, crud_event, False, obj.is_staff,
                  obj.is_active, obj.is_marketing]
        cursor.execute(
            "{call dbo.mg_CRUD_UserManagement(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s)}",
            params)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        # Only show the accounts which are admins or staff
        return super().get_queryset(request).using(self.using).filter(is_staff=True)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


admin.site.register(Account, UserDBModelAdmin)
admin.site.unregister(Group)
