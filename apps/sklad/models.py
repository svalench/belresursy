from django.db import models

# Create your models here.

class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Наименование', max_length=255)
    description = models.TextField('Описание', default=None)
    address = models.TextField('Адрес', default=None)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    unp = models.CharField('УНП', max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'

