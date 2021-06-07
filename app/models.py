from django.db import models


class TopManager(models.Model):
    name = models.CharField("Имя", max_length=100, db_index=True, unique=True)
    position = models.CharField("Должность", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Топ-менеджер'
        verbose_name_plural = 'Топ-менеджеры'


class Organization(models.Model):
    name = models.CharField("Название организации", max_length=100, db_index=True, unique=True)
    date = models.DateField("Дата создания организации", blank=True, null=True)
    topmanager = models.ManyToManyField(TopManager)
    fieldactivity = models.CharField("Сферы деятельности организации", max_length=100)
    location = models.CharField("Местоположение головного офиса", max_length=100)
    slink = models.URLField("Cсылка на официальный сайт", blank=True)
    plink = models.URLField("Профили в социальных сетях", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
