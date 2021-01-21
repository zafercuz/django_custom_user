from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from account.managers import MyAccountManager


class Account(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    TID = models.AutoField(_('table id'), auto_created=True, primary_key=True)
    Emp_ID = models.CharField(_('employee id'), max_length=10, unique=True, error_messages={
        'unique': _("A user with that username already exists."),
    }, )
    username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        db_column='Username'
    )
    password = models.CharField(_('password'), max_length=128, db_column='myPassword')
    FName = models.CharField(_('first name'), max_length=50, blank=True, null=True)
    MI = models.CharField(_('middle initial'), max_length=50, blank=True, null=True)
    LName = models.CharField(_('last name'), max_length=50, blank=True, null=True)
    Designation = models.CharField(_('designation'), max_length=50, blank=True, null=True)
    Office = models.CharField(_('office'), max_length=50, blank=True, null=True)
    Department = models.CharField(_('department'), max_length=50, blank=True, null=True)
    BranchCode = models.CharField(_('branch code'), max_length=10)
    email = models.EmailField(_('email'), max_length=50, unique=True, db_column='Email_Address')
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_('Designates whether this user should be treated as a superuser.'),
    )
    is_admin = models.BooleanField(
        _('admin status'),
        default=False,
        help_text=_('Designates whether this user should be treated as an admin.'),
        db_column='Is_Admin'
    )
    is_hr = models.BooleanField(
        _('hr status'),
        default=False,
        help_text=_('Designates whether this user should be treated as a HR.'),
        db_column='Is_HR'
    )
    is_LMS = models.BooleanField(
        _('lms status'),
        default=False,
        help_text=_('Designates whether this user should be treated as a lms.'),
        db_column='Is_LMS'
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_marketing = models.BooleanField(
        _('marketing'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as marketing team.'
        ),
    )
    IPAdd_Login = models.GenericIPAddressField(_('ip address login'), blank=True, null=True)
    IsOnline = models.BooleanField(_('is online'), default=False,
                                   help_text=_('Designates whether the user is online.'))
    Machine = models.CharField(max_length=20, blank=True, null=True)
    Product_Version = models.CharField(max_length=20, blank=True, null=True)
    is_approver = models.BooleanField(
        _('approver'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as an approver.'
        ),
        db_column='is_approver'
    )
    Company = models.CharField(max_length=100, blank=True, null=True)
    is_inquiry = models.BooleanField(
        _('inquiry'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as an inquiry.'
        ),
        db_column='Is_Inquiry'
    )
    TransactedBy = models.CharField(max_length=50, blank=True, null=True)
    PostingDate = models.DateTimeField(_('posting date'), blank=True, null=True)
    Reset_Pass = models.BooleanField(default=False, blank=True, null=True)
    UFullName = models.CharField(max_length=100, blank=True, null=True)
    BranchName = models.CharField(max_length=50, blank=True, null=True)
    CCode = models.CharField(max_length=10, blank=True, null=True)
    Is_UniformMgmt = models.BooleanField(default=False, blank=True, null=True)
    Is_Insurance = models.BooleanField(default=False, blank=True, null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        db_table = 'UserManagement'
