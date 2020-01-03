from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from apps.sklad.models import Agent
from setting_common import USER_ROLES_FOR_REDIRECTS_CHOICES


class GroupUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Нзвание группы', max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.CharField(max_length=20, choices=USER_ROLES_FOR_REDIRECTS_CHOICES,
                                 verbose_name='Роль пользователя', default=USER_ROLES_FOR_REDIRECTS_CHOICES[0][0])

    def __str__(self):
        return self.user_role


class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, default=None)
    number = models.DateTimeField('Номер', max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда', default=None)
    last_out = models.DateTimeField('время последнего выезда', default=None)
    ves_in = models.FloatField('вес на въезде', default=None)
    ves_out = models.FloatField('вес на выезде', default=None)
    netto_last = models.FloatField("полсденее нетто", default=None)
    netto1 = models.FloatField("нетто препоследнее", default=None)
    netto2 = models.FloatField("нетто предпред последнее", default=None)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Pricep(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, default=None)
    number = models.DateTimeField('Номер', max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда', default=None)
    last_out = models.DateTimeField('время последнего выезда', default=None)
    ves_in = models.FloatField('вес на въезде', default=None)
    ves_out = models.FloatField('вес на выезде', default=None)
    netto_last = models.FloatField("полсденее нетто", default=None)
    netto1 = models.FloatField("нетто предпоследнее", default=None)
    netto2 = models.FloatField("нетто предпред последнее", default=None)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Прицеп'
        verbose_name_plural = 'Прицепы'

class Vagon(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, default=None)
    number = models.DateTimeField('Номер', max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда', default=None)
    last_out = models.DateTimeField('время последнего выезда', default=None)
    ves_in = models.FloatField('вес на въезде', default=None)
    ves_out = models.FloatField('вес на выезде', default=None)
    netto_last = models.FloatField("полсденее нетто", default=None)
    netto1 = models.FloatField("нетто предпоследнее", default=None)
    netto2 = models.FloatField("нетто предпред последнее", default=None)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Вагон'
        verbose_name_plural = 'Вагоны'