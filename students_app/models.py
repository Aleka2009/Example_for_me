from django.db import models

# student_class:
# 	first_name
# 	last_name
# 	date_of_birth
# 	phone_number
# 	email
# 	gender
# 	id_course

from courses_app.models import Course
from employees_app.models import Communism

class Student(Communism, models.Model):
    id_course = models.ManyToManyField(Course)

    class Meta:
        ordering = ['second_name']
        """If i have not a front dev """
        # unique_together = (
        #     'first_name',
        #     'second_name',
        #     'date_of_birth',
        #     'email',
        # )

    def __str__(self):
        return f'{self.second_name}' f' {self.first_name}'


    """First variation"""
    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'second_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Student, self).save(*args, **kwargs)
