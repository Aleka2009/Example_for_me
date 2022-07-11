from django.contrib import admin

from employees_app.models import Employee, Department, Position


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)

