from django.contrib.postgres.fields import JSONField
from django.db import models

from django import urls


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{0}'.format(self.name)


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        null=False
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    characteristics = JSONField()
    price = models.FloatField(
        null=False
    )

    def get_absolute_url(self):
        return urls.reverse('detail', args=[str(self.id)])

    def __str__(self):
        return '{0},{1]'.format(self.name, self.price)
