from django.db import models

TYPE_OF_CP_CHOICES = (
    ('1', u'Физическое Лицо'),
    ('2', u'Юридическое лицо'),
)


# Create your models here.

class Manager(models.Model):
    manager_name =  models.CharField(max_length=256)
    def __str__(self):
       return self.manager_name

class Cities(models.Model):
    name = models.CharField(max_length=256)
    def __str__(self):
       return self.name

class TypeOfService(models.Model):
    type_of_service = models.CharField(max_length=256)
    def __str__(self):
       return self.type_of_service

class Channel(models.Model):
    channel = models.CharField(max_length=256)
    def __str__(self):
       return self.channel

class KnowsFrom(models.Model):
    knows_from = models.CharField(max_length=256)
    def __str__(self):
       return self.knows_from

class TypeOfCP(models.Model):
    type_of_cp = models.CharField(max_length=256)
    def __str__(self):
       return self.type_of_cp

class Counterparties(models.Model):
    name = models.CharField(max_length=256, verbose_name='Наименование контрагента')
    type_of_counterparties = models.ForeignKey(TypeOfCP, default=None, verbose_name='Тип контрагента', on_delete=models.CASCADE)
    vip = models.BooleanField(default=False, verbose_name='ВИП Клиент')
    city = models.ForeignKey(Cities, default=None, verbose_name='Нас. пункт', related_name='cities',on_delete=models.CASCADE)
    typeOfService = models.ForeignKey(TypeOfService, default=None, verbose_name='Тип услуги', on_delete=models.CASCADE)
    address_from = models.CharField(max_length=1024, verbose_name='Адрес VLAN От')
    address_to = models.CharField(max_length=1024, verbose_name='До')
    channel = models.ForeignKey(Channel, default=None, verbose_name='Ширина канала', on_delete=models.CASCADE)
    ticketDate = models.DateField(verbose_name='Дата заявки', default=None)
    knowsFrom = models.ForeignKey(KnowsFrom, default=None, verbose_name='Откуда узнали об услугах', on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, default=None, verbose_name='Менеджер', on_delete=models.CASCADE)

    def __str__(self):
       return self.name



