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
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, null=True)
    number = models.CharField('Номер', max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда', null=True)
    last_out = models.DateTimeField('время последнего выезда',  null=True)
    ves_in = models.FloatField('вес на въезде',  null=True)
    ves_out = models.FloatField('вес на выезде', null=True)
    nakladnaya = models.CharField('Накладная', max_length=255, default=0)
    netto_last = models.FloatField("полсденее нетто",  null=True)
    netto1 = models.FloatField("нетто препоследнее",  null=True)
    netto2 = models.FloatField("нетто предпред последнее",  null=True)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

class Pricep(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, null=True)
    number = models.CharField('Номер', max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда',  null=True)
    last_out = models.DateTimeField('время последнего выезда',  null=True)
    ves_in = models.FloatField('вес на въезде',   null=True)
    ves_out = models.FloatField('вес на выезде',  null=True)
    netto_last = models.FloatField("полсденее нетто",  null=True)
    netto1 = models.FloatField("нетто предпоследнее",  null=True)
    netto2 = models.FloatField("нетто предпред последнее",  null=True)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Прицеп'
        verbose_name_plural = 'Прицепы'

class Vagon(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, null=True)
    number = models.CharField('Номер', max_length=255)
    nakladnaya = models.CharField('Накладная', max_length=255, default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    last_in = models.DateTimeField('время последнего въезда',  null=True)
    last_out = models.DateTimeField('время последнего выезда', null=True)
    ves_in = models.FloatField('вес на въезде',  null=True)
    ves_out = models.FloatField('вес на выезде',  null=True)
    netto_last = models.FloatField("полсденее нетто", null=True)
    netto1 = models.FloatField("нетто предпоследнее",  null=True)
    netto2 = models.FloatField("нетто предпред последнее",  null=True)
    status_in = models.BooleanField('На территории?', default= False)
    def __str__(self):
        return self.number
    class Meta:
        verbose_name = 'Вагон'
        verbose_name_plural = 'Вагоны'