from django.db import connections
from django.http import HttpResponse
from account.models import Account


def dict_fetch_all(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def connect_user(self):
    # with connections['other_db'].cursor() as cursor:
    #     cursor.execute("SELECT * FROM dbo.UserManagement")
    #     result = cursor.fetchall()
    # print(result)

    cursor = connections['other_db'].cursor()
    try:
        # cursor.execute("{call dbo.mg_losignin(%s,%s,%s)}", ["mndavid", "123", None])
        params = ["000", "admin", "123", "Michael Steven", "N", "David", "13070", None, None, None, None, None, None,
                  "admin@hondamotorworld.com", False, True, True, False, False, False, False, None, "CREATE", False]
        cursor.execute(
            "{call dbo.mg_CRUD_UserManagement(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)}",
            params)
        result_set = dict_fetch_all(cursor)

    finally:
        cursor.close()

    # Defer means to exclude column fields from the Account Model
    # user = Account.objects.using("other_db").all()
    # print(user)
    return HttpResponse("Hello World")
