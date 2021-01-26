from django.contrib.auth.backends import ModelBackend
from django.db import connections

from .models import Account


def dict_fetch_all(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


class CustomAccountBackend(ModelBackend):
    """
    Custom authentication where it uses stored procedures for logging in
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = username  # Set it to username since we defined USERNAME_FIELD = email
        password = password
        cursor = connections['other_db'].cursor()
        try:
            account = Account.objects.using("other_db").get(email=email)
            # Query the Account then use the account's username to check if credentials are correct
            cursor.execute("{call dbo.mg_losignin(%s,%s,%s)}", [account.username, password, None])
            result_set = dict_fetch_all(cursor)
            # 0 = AUTHENTICATE || 1 = ERROR
            if result_set[0]['Status'] == 0 and self.user_can_authenticate(account):
                return account
        except Account.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            user = Account.objects.using("other_db").get(pk=user_id)
        except Account.DoesNotExist:
            return None
        return user if self.user_can_authenticate(user) else None
