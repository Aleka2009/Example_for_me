from students_app.models import Student
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class StudentSerializer(serializers.ModelSerializer):
    employee_first_name = serializers.CharField(read_only=True)
    employee_last_name = serializers.CharField(read_only=True)
    employee_phone_number = serializers.CharField(read_only=True)
    employee_email = serializers.CharField(read_only=True)
    course_name = serializers.CharField(read_only=True)

    # 'employee_first_name', 'employee_last_name', 'employee_phone_number',
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course',
                  'employee_first_name', 'employee_last_name', 'employee_phone_number', 'employee_email', 'course_name']
        extra_kwargs = {'user': {'read_only': True}}
        """If front have method POST"""

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Student.objects.all(),
        #         fields=['first_name', 'last_name', 'date_of_birth', 'email']
        #     )
        # ]

    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     serializers_user = StudentSerializer(instance=instance.user)
    #     response["user"] = serializers_user.data
    #     return response
