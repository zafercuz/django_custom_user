from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, PasswordChangeForm
from django.db import connections

from account.backends import dict_fetch_all
from account.models import Account


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)

        # Do the Stored Procedure of saving/editing a User here instead of having "user.set_password"
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'password', 'is_active', 'is_staff')

    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value
    #     return self.initial["password"]


class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_old_password(self):
        """
        Validate that the old_password field is correct but using the stored procedure
        """
        cursor = connections['other_db'].cursor()
        old_password = self.cleaned_data["old_password"]
        account: Account = self.user
        cursor.execute("{call dbo.mg_CheckPassword(%s,%s)}", [account.username, old_password])
        result_set = dict_fetch_all(cursor)
        if result_set[0]['Status'] == 1:
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password
