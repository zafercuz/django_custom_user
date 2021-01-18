from django.contrib.auth.backends import ModelBackend
from .models import Account


class CustomAccountBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = username  # Set it to username since we defined USERNAME_FIELD = email
        password = password
        try:
            account = Account.objects.using("other_db").get(email=email)
            if account.check_password(password) and self.user_can_authenticate(account):
                return account
        except Account.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            user = Account.objects.using("other_db").get(pk=user_id)
        except Account.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
