from rest_framework.serializers import ModelSerializer
from .Database import DepartmentModel
class DepartmentSerializer(ModelSerializer):
    class Meta:
        model=DepartmentModel
        fields="__all__"
