from django.db import connections
from django.http import HttpResponse
from account.models import Account


def connect_user(self):
    # with connections['other_db'].cursor() as cursor:
    #     cursor.execute("SELECT * FROM dbo.UserManagement")
    #     result = cursor.fetchall()
    # print(result)

    # Defer means to exclude column fields from the Account Model
    user = Account.objects.using("other_db").all()
    print(user)
    return HttpResponse("Hello World")
