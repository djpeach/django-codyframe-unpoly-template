from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.accounts.helpers.user_helpers import make_username


class User(AbstractUser):
    """
    https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    REQUIRED_FIELDS _only_ controls the `createsuperuser` command. By default, it requires email
    By setting it to a blank list, it will no longer require email. Username and
    password, however, are always required, regardless of this value.
    """

    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username} - {self.get_full_name()}"


class Staff(User):
    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    user = models.OneToOneField(
        get_user_model(), parent_link=True, primary_key=True, on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Customer(User):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    class CustomerType(models.TextChoices):
        RETAIL = "RETAIL", "Retail Customer"
        DEALER = "DEALER", "Dealer"  # reseller
        OEM = "OEM", "OEM (Manufacturer)"  # manufacturer

    user = models.OneToOneField(
        get_user_model(), parent_link=True, primary_key=True, on_delete=models.CASCADE
    )
    customer_type = models.CharField(
        max_length=24, choices=CustomerType.choices, default=CustomerType.RETAIL
    )
    company_name = models.CharField(max_length=80, null=True, blank=True)
    phone = models.CharField(max_length=24, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = make_username(self.email)
        super().save(*args, **kwargs)
