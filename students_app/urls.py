from django.urls import path
from students_app.views import StudentViewSet, StudentViewSet

urlpatterns = [
    # for StudentViewSet
    # path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('create/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('create/<int:pk>/', StudentViewSet.as_view(
        {'get': 'retrieve', 'put': 'update'}
    )),
]