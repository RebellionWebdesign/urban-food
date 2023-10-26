from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """
    Custom manager for the User model. Instead of the username field,
    the email field is used as the identifier.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a user.
        """
        if not email:
            raise ValueError("Please provide an email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a super user.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Please set is_staff to True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Please set is_superuser to True")
        return self.create_user(email, password, **extra_fields)