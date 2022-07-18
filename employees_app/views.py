from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from employees_app.models import Employee, Department, Position
from employees_app.serializers import DepartmentSerializer, EmployeeSerializer, PositionSerializer
from rest_framework import viewsets


"""
CRUD 
C = CREATE
R = RETRIEVE
U = UPDATE
D = DESTROY
"""


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['id', 'name']
    ordering_fields = ['name']


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['department']
    search_fields = ['id', 'name']
    ordering_fields = ['name']


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    ordering_fields = ['user']
    search_fields = ['user__username']
    filterset_fields = ['position']
