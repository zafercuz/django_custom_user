from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db import connections
from django.http import HttpResponse
from django.contrib.auth.views import PasswordContextMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView

from account.forms import CustomPasswordChangeForm
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
                  "admin@hondamotorworld.com", False, True, True, False, False, False, False, None, "CREATE", False,
                  True, True, False]
        cursor.execute(
            "{call dbo.mg_CRUD_UserManagement(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s)}",
            params)
        result_set = dict_fetch_all(cursor)

    finally:
        cursor.close()

    return HttpResponse("Hello World")


class CustomPasswordChangeView(PasswordContextMixin, SuccessMessageMixin, FormView):
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('admin:index')
    template_name = 'registration/password_change_form.html'
    success_message = "Password successfully changed, please login again"
    title = _('Password change')

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        cursor = connections['other_db'].cursor()
        account: Account = self.request.user
        cursor.execute("{call dbo.mg_UpdateUserPassword(%s,%s)}",
                       [account.username, form.cleaned_data['new_password1']])
        result_set = dict_fetch_all(cursor)
        if result_set[0]['Status'] == 1:
            raise Exception('500 error')
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)
