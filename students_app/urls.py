from django.urls import path
from students_app.views import StudentViewSet, StudentViewSet

urlpatterns = [
    # for StudentViewSet
    # path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('student/create/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('student/create/<int:pk>/', StudentViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'update'}
    )),
]