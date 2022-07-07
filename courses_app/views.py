from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from courses_app.models import Course
from courses_app.serializers import CourseSerializer
from rest_framework import viewsets

"""If you have not front-dev or do not want """
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    """Information about courses for front_dev"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseView(ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id', 'name', 'duration', 'price', 'is_active']
    ordering_fields = ['price']
