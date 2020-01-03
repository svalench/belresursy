from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from setting_common import USER_ROLES_FOR_REDIRECTS_CHOICES


class GroupUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Нзвание группы', max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Цех'
        verbose_name_plural = 'Цеха'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=20, choices=USER_ROLES_FOR_REDIRECTS_CHOICES,
                                 verbose_name='Роль пользователя', default=USER_ROLES_FOR_REDIRECTS_CHOICES[0][0])

    def __str__(self):
        return self.user_role