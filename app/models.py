from django.db import models


class FieldOfActivity(models.Model):
    name = models.CharField("Сфера деятельности организации", max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сферы деятельности'

class Link(models.Model):
    slink = models.URLField("Cсылка на официальный сайт", blank=True)
    plink = models.URLField("Профили в социальных сетях", blank=True)

    def __str__(self):
        return self.slink

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

class Organization(models.Model):
    name = models.CharField("Название организации", max_length=100, db_index=True, unique=True)
    date = models.DateField("Дата создания организации", blank=True, null=True)
    # topmanager = models.ManyToManyField(TopManager)
    field = models.ManyToManyField(FieldOfActivity)
    location = models.CharField("Местоположение головного офиса", max_length=100)
    link = models.ForeignKey(Link, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class TopManager(models.Model):
    name = models.CharField("Имя",max_length=100, db_index=True, unique=True)
    position = models.CharField("Должность", max_length=100)
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Топ-менеджер'
        verbose_name_plural = 'Топ-менеджеры'


