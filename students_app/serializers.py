from students_app.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'second_name', 'date_of_birth', 'phone_number', 'email', 'gender']

