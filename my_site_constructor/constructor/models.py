from django import urls
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models import Q


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


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
                blank=True
    )
    big_photo_link = models.FileField(
                max_length=500,
                null=False,
                blank=True
    )
    price = models.FloatField(
        null=False
    )

    def get_absolute_url(self):
        return urls.reverse('detail', args=[str(self.category_id), str(self.id)])

    def __str__(self):
        return f'{self.name}'


class Setup(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    cpu = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=1),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_cpu'
    )

    motherboard = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=2),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_motherboard'
    )

    video_card = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=3),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_video_card'
    )

    ram = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=4),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_ram'
    )

    cooler = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=5),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_cooler'
    )

    hdd = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=6),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_hdd'
    )

    dvd = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=7),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_dvd'
    )

    power = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=8, name__contains='Блок питания'),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_power'
    )

    case = models.ForeignKey(
        Product,
        limit_choices_to=Q(category_id=8, name__contains='Корпус'),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='users_case'
    )
