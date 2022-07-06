from courses_app.models import Course
from courses_app.serializers import CourseSerializer
from rest_framework import viewsets


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Information about courses for front_dev"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
