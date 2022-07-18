from auth_app.serializers import UserSerializer
from employees_app.models import Employee, Department, Position
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        serializers_user = UserSerializer(instance=instance.user)
        response["user"] = serializers_user.data
        return response
