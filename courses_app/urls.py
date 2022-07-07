from django.urls import path
from courses_app.views import CourseViewSet, CourseView

urlpatterns = [
    # for CourseViewSet
    # path('', CourseViewSet.as_view({'get': 'list', 'post': 'create'}), name='course-list'),
    path('course/create/', CourseView.as_view({'get': 'list', 'post': 'create'})),
    path('course/create/<int:pk>/', CourseView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
]