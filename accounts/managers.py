from django.contrib.auth.models import BaseUserManager

class UserPasswordManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, date_of_birth, password=None, **extra_fields):
        full_name = f"{first_name}{last_name}".lower()
        if password is None:
            password = f"{full_name[:4]}{date_of_birth:%d%m}"
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name='', last_name='', date_of_birth=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, first_name, last_name, date_of_birth, password, **extra_fields)
        