from django.urls import path
from schools_app.views import SchoolViewSet

urlpatterns = [
    path('school/', SchoolViewSet.as_view({'get': 'list'}), name='school-list'),
]
