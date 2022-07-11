from django.urls import path
from employees_app.views import EmployeeViewSet, DepartmentViewSet, PositionViewSet

urlpatterns = [
    path('employee/create/', EmployeeViewSet.as_view({'get': 'list', 'post': 'create'}), name='employee-list'),
    path('employee/create/<int:pk>/', EmployeeViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'update'}
    ),
        name='employee-list-create'
         ),
    path('department/', DepartmentViewSet.as_view({'get': 'list'}), name='department-list'),
    path('position/', PositionViewSet.as_view({'get': 'list'}), name='position-list'),
]
