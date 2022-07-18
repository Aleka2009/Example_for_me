from courses_app.models import Course
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'duration', 'price', 'is_active', 'school']

        """If front have method POST"""

        validators = [
            UniqueTogetherValidator(
                queryset=Course.objects.all(),
                fields=['name', 'duration', 'price']
            )
        ]
