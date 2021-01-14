from django.contrib.auth.backends import ModelBackend
from .models import Account


class CustomAccountBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        # Get the email field, it's called username as we set the username_field in models to be the email address
        email = kwargs['username']
        password = kwargs['password']
        try:
            account = Account.objects.get(email=email)
            if account.check_password(password) is True:
                return account
        except Account.DoesNotExist:
            pass
