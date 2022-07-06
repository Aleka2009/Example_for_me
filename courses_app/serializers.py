from rest_framework.validators import UniqueTogetherValidator

from courses_app.models import Course
from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'price', 'is_active']

        """If front have method POST"""
        from rest_framework.validators import UniqueTogetherValidator

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Course.objects.all(),
        #         fields=['name', 'duration', 'price']
        #     )
        # ]

