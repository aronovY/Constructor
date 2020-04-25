from django.db import models
from django.contrib.postgres.fields import JSONField
from django import urls


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{0}'.format(self.name)


class Product(models.Model):
    name = models.CharField(
        max_length=300,
        null=False,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    characteristics = JSONField()
    small_photo_link = models.FileField(
                max_length=500,
                null=False,
                blank=True)
    big_photo_link = models.FileField(
                max_length=500,
                null=False,
                blank=True)
    price = models.FloatField(
        null=False
    )

    def get_absolute_url(self):
        return urls.reverse('detail', args=[str(self.category_id), str(self.id)])

    def __str__(self):
        return f'{self.name}'
