from students_app.models import Student
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'second_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course']

        """If front have method POST"""

        validators = [
            UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=['first_name', 'second_name', 'date_of_birth', 'email']
            )
        ]
