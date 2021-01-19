class DontLog:
    """
    This class makes it so that it wont record logs, since there will be an error conflict for USER since we are
    authenticating from another database. Hence we will have an error for logs since the logs will be stored in the
    default database rather and a user doesn't exist in the default database
    """
    def log_addition(self, *args):
        return

    def log_change(self, *args):
        return

    def log_deletion(self, *args):
        return
