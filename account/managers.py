from django.contrib.auth.base_user import BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    # def create_user(self, email, username, password=None):
    #     print("create user")
    #     if not email:
    #         raise ValueError("Users must have an email address")
    #     if not username:
    #         raise ValueError("Users must have an username")
    #
    #     user = self.model(
    #         Email_Address=self.normalize_email(email),
    #         Username=username
    #     )
    #
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_superuser(self, email, username, password):
    #     print("Create super user")
    #     if password is None:
    #         raise TypeError('Superusers must have a password.')
    #     user = self.create_user(
    #         email=self.normalize_email(email),
    #         password=password,
    #         username=username
    #     )
    #     user.is_admin = True
    #     user.is_staff = True
    #     user.is_superuser = True
    #     user.save(using=self._db)
