from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def connect_user(self):
    with connections['other_db'].cursor() as cursor:
        cursor.execute("SELECT * FROM dbo.UserManagement")
        result = cursor.fetchall()
    print(result)
    print("Try connect here")
    return HttpResponse("Hello World")
