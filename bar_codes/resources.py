from import_export import resources
from .models import BarCodeModel


class BarCodeResource(resources.ModelResource):
    class Meta:
        model = BarCodeModel
