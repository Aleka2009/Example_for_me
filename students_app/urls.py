from django.urls import path
from students_app.views import StudentViewSet

urlpatterns = [
    path('', StudentViewSet.as_view({'get': 'list'}), name='student-list'),
]