from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.sessions.models import Session
from hijack.contrib.admin import HijackUserAdminMixin

from apps.accounts.models.user_models import User, Customer, Staff


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(HijackUserAdminMixin, DjangoUserAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(HijackUserAdminMixin, DjangoUserAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(HijackUserAdminMixin, DjangoUserAdmin):
    pass
