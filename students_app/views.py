from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework import viewsets

"""If you have not front-dev or do not want """


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    """Information about courses for front_dev"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['id', 'first_name', 'second_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course']
