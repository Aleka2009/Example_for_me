from django.db import models
from employees_app.models import Employee

# student_class:
# 	first_name
# 	last_name
# 	date_of_birth
# 	phone_number
# 	email
# 	gender
# 	id_course
from auth_app.models import MyUser
from courses_app.models import Course
# from employees_app.models import Employee
# from employees_app.models import Communism


class Student(models.Model):
    GENDER_CHOICES = (
        ('female', 'female'),
        ('male', 'male'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    course = models.ManyToManyField(Course, related_name='course')
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
    )
    user = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)

    #
    # class Meta:
    #     ordering = ['last_name']
    #     """If i have not a front dev """
# unique_together = (
#     'first_name',
#     'second_name',
#     'date_of_birth',
#     'email',
# )

    def __str__(self):
        return f'{self.last_name}' f' {self.first_name}'


    """First variation"""
    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Student, self).save(*args, **kwargs)

