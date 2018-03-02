from django.db import models
from django.template.defaultfilters import slugify


class BarCodeModel(models.Model):
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    dependence = models.CharField(max_length=255)
    headquarters = models.CharField(max_length=255)
    bar_code = models.ImageField(
        blank=True,
        null=True,
        upload_to='bar_code',
    )

    def get_code(self):
        self.code

    def get_name(self):
        self.name

    class Meta:
        db_table = 'bar_codes'

