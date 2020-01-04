from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User

from apps.vesovay.models import *


class EmployeeInline(admin.StackedInline):
    model = Client
    verbose_name_plural = 'permissions'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(GroupUser)
admin.site.register(Auto)