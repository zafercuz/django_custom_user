from django.db import connections
from django.http import HttpResponse
from account.models import Account


def connect_user(self):
    # with connections['other_db'].cursor() as cursor:
    #     cursor.execute("SELECT * FROM dbo.UserManagement")
    #     result = cursor.fetchall()
    # print(result)

    cursor = connections['other_db'].cursor()
    try:
        user_list = []
        cursor.execute("{call dbo.mg_ShowUserByUname(%s)}", ["admin"])
        result_set = cursor.fetchall()
        if result_set:
            user = Account()
            for result in result_set:
                user.TID = result[0]
                user.Emp_ID = result[1]
                user.username = result[2]
                user.FName = result[3]
                user.MI = result[4]
                user.LName = result[5]
                user.password = result[6]
                user.Designation = result[7]
                user.Office = result[8]
                user.Department = result[9]
                user.BranchCode = result[10]
                user.email = result[11]
                user.is_superuser = result[12]
                user.is_admin = result[13]
                user.is_hr = result[14]
                user.is_LMS = result[15]
                user.last_login = result[16]
                user.IPAdd_Login = result[17]
                user.IsOnline = result[18]
                user.Machine = result[19]
                user.Product_Version = result[20]
                user.is_approver = result[21]
                user.Company = result[22]
                user.is_inquiry = result[23]
                user.TransactedBy = result[24]
                user.PostingDate = result[25]
                user.Reset_Pass = result[26]
                user.UFullName = result[27]
                user.BranchName = result[28]
                user.CCode = result[29]
                user.Is_UniformMgmt = result[30]
                user.Is_Insurance = result[31]
                user.is_staff = result[32]
                user.is_active = result[33]
                user.is_marketing = result[34]
                user_list.append(user)

            print(user_list)
    finally:
        cursor.close()

    # Defer means to exclude column fields from the Account Model
    # user = Account.objects.using("other_db").all()
    # print(user)
    return HttpResponse("Hello World")
