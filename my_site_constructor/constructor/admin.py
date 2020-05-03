from django.contrib import admin
from django.contrib.postgres.fields import JSONField

from constructor.models import Product, Setup
from constructor.utils import ReadableJSONFormField

admin.site.register(Setup)


@admin.register(Product)
class ExampleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'form_class': ReadableJSONFormField},
    }
