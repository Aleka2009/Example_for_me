from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework import viewsets

"""If you have not front-dev or do not want """


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """Information about courses for front_dev"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['id', 'first_name', 'second_name']
    ordering_fields = ['first_name']
