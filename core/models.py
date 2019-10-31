from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import unidecode


# Create your models here.
class Indicator(models.Model):
    group = models.CharField(max_length=200, verbose_name='Группа')
    name = models.CharField(max_length=200, verbose_name='Показатель')

    class Meta:
        ordering = ('group',)
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'

    def __str__(self):
        return '{} {}'.format(self.group, self.name)


class Office(models.Model):
    id = models.SmallIntegerField(primary_key=True, verbose_name='Офис')
    department = models.CharField(max_length=200, verbose_name='ТО')
    city = models.CharField(max_length=200, verbose_name='Город')
    slug = models.SlugField(max_length=200, verbose_name='URL', blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

    def save(self, *args, **kwargs):
        url = unidecode.unidecode(self.department)
        self.slug = slugify(url)
        return super(Office, self).save(*args, *kwargs)

    def __str__(self):
        return '{} {} {}'.format(self.department, self.city, self.id)


class Dynamic(models.Model):
    indicator = models.ForeignKey(Indicator,
                                  on_delete=models.CASCADE,
                                  related_name='dynamic',
                                  verbose_name='Показатель')
    office = models.ForeignKey(Office,
                               on_delete=models.CASCADE,
                               related_name='dynamic',
                               verbose_name='Офис')
    month = models.DateField(verbose_name='Месяц')
    value = models.BigIntegerField(verbose_name='Значение')

    class Meta:
        ordering = ('month',)
        verbose_name = 'Динамика показателей'
        verbose_name_plural = 'Динамика показателей'
