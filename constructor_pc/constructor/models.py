from django.contrib.postgres.fields import JSONField
from django.db import models

from django import urls


class Category(models.Model):
    name = models.CharField(max_length=100)


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
        return urls.reverse('cpu-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}'.format(self.name)


# class VideoCard(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('videocard-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)
#
#
# class Motherboard(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('motherboard-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)
#
#
# class Ram(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('ram-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)
#
#
# class Cooler(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('cooler-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)
#
#
# class PowerSupply(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('power_supply-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)
#
#
# class Case(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('case-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)
#
#
# class Hdd(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('hdd-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)
#
#
# class Dvd(models.Model):
#     name = models.CharField(
#         max_length=128,
#         null=False
#     )
#     characteristics = JSONField()
#     price = models.FloatField(
#         null=False
#     )
#
#     def get_absolute_url(self):
#         return urls.reverse('hdd-detail', args=[str(self.id)])
#
#     def __str__(self):
#         return '{0}'.format(self.name)