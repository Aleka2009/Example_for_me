from django.urls import path
from students_app.views import StudentViewSet, StudentView

urlpatterns = [
    # for StudentViewSet
    # path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('student/create/', StudentView.as_view({'get': 'list', 'post': 'create'})),
    path('student/create/<int:pk>/', StudentView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
]