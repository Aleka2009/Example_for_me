from django.db import models

# Courses_app:
#     course class:
# 		name
# 		duration
# 		price
# 		is_active
from schools_app.models import School


class Course(models.Model):
    TYPE_CHOICES = (
        ('OFFLINE', 'offline'),
        ('ONLINE', 'online'),
        ('-', '-'),
    )

    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    id_school = models.ForeignKey(School, on_delete=models.CASCADE)
    max_student = models.PositiveIntegerField()
    type_of_education = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        default='-'
    )

    class Meta:
        ordering = ['name']
        """If i have not a front dev """
        # unique_together = (
        #     'name',
        #     'duration',
        #     'price',
        # )

    def __str__(self):
        return self.name

    def save(self, *args):
        for field_name in ['name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Course, self).save(*args)
