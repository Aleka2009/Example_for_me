from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from employees_app.permissions import EmployeePermission
from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Prefetch, F, Count

"""If you have not front-dev or do not want """


# class StudentViewSet(viewsets.ReadOnlyModelViewSet):
#     """Information about courses for front_dev"""
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['course']
    search_fields = ['id', 'first_name', 'last_name']
    ordering_fields = ['first_name']
    permission_classes = (EmployeePermission, IsAuthenticated)

    def get_queryset(self):
        queryset = Student.objects.annotate(
            employee_first_name=F('user__employee__first_name'),
            employee_last_name=F('user__employee__last_name'),
            employee_phone_number=F('user__employee__phone_number'),
            employee_email=F('user__email'),
            course_name=F('course__name'),
        ).order_by('-id')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
