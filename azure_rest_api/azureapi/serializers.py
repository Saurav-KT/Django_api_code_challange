from rest_framework import serializers
from .models import EmpDetails


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpDetails
        fields = "__all__"