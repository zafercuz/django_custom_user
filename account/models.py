from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Account(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    TID = models.IntegerField(_('table id'), primary_key=True)
    Emp_ID = models.CharField(_('employee id'), max_length=10, unique=True, error_messages={
        'unique': _("A user with that username already exists."),
    }, )
    Username = models.CharField(
        _('username'),
        max_length=50,
        unique=True,
        help_text=_('Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    FName = models.CharField(_('first name'), max_length=50, blank=True, null=True)
    MI = models.CharField(_('middle initial'), max_length=50, blank=True, null=True)
    LName = models.CharField(_('last name'), max_length=50, blank=True, null=True)
    Designation = models.CharField(_('designation'), max_length=50, blank=True, null=True)
    Office = models.CharField(_('office'), max_length=50, blank=True, null=True)
    Department = models.CharField(_('department'), max_length=50, blank=True, null=True)
    BranchCode = models.CharField(_('branch code'), max_length=10)
    Email_Address = models.EmailField(_('email'), max_length=50, unique=True)
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        help_text=_('Designates whether this user should be treated as a superuser.'),
    )
    Is_Admin = models.BooleanField(
        _('admin status'),
        default=False,
        help_text=_('Designates whether this user should be treated as an admin.'),
    )
    Is_HR = models.BooleanField(
        _('hr status'),
        default=False,
        help_text=_('Designates whether this user should be treated as a HR.'),
    )
    Is_LMS = models.BooleanField(
        _('lms status'),
        default=False,
        help_text=_('Designates whether this user should be treated as a lms.'),
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
    IPAdd_Login = models.GenericIPAddressField(_('ip address login'), blank=True, null=True)
    IsOnline = models.BooleanField(_('is online'), default=False,
                                   help_text=_('Designates whether the user is online.'))
    Machine = models.CharField(max_length=20, blank=True, null=True)
    Product_Version = models.CharField(max_length=20, blank=True, null=True)
    Is_Approver = models.BooleanField(
        _('approver'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as an approver.'
        ),
    )
    Company = models.CharField(max_length=100, blank=True, null=True)
    Is_Inquiry = models.BooleanField(
        _('inquiry'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as an inquiry.'
        ),
    )
    TransactedBy = models.CharField(max_length=50, blank=True, null=True)
    PostingDate = models.DateTimeField(_('posting date'), blank=True, null=True)
    Reset_Pass = models.BooleanField(default=False, blank=True, null=True)
    UFullName = models.CharField(max_length=100, blank=True, null=True)
    BranchName = models.CharField(max_length=50, blank=True, null=True)
    CCode = models.CharField(max_length=10, blank=True, null=True)
    Is_UniformMgmt = models.BooleanField(default=False, blank=True, null=True)
    Is_Insurance = models.BooleanField(default=False, blank=True, null=True)

    EMAIL_FIELD = 'Email_Address'
    USERNAME_FIELD = 'Email_Address'
    REQUIRED_FIELDS = ['Username']

    objects = MyAccountManager()

    def __str__(self):
        return self.Email_Address

    def has_perm(self, perm, obj=None):
        return self.Is_Admin

    def has_module_perms(self, app_label):
        return True
