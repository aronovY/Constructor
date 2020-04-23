from django.contrib import admin
from constructor.models import Product, Category
from django.contrib.postgres.fields import JSONField
from constructor.utils import ReadableJSONFormField


@admin.register(Product)
class ExampleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'form_class': ReadableJSONFormField},
    }
