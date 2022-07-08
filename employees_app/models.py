from django.db import models

# employee_class:
# 		first_name
# 		second_name
# 		date_of_birth
# 		phone_number
# 		email
# 		gender
# 		id_position(ForeignKey)
# 		salary
# 	department_class:
# 		name
# 		description
# 		id_school(ForeignKey)
# 	position_class:
# 		name
# 		duration
# 		description
# 		is_active
# 		permission
# 		id_department(ForeignKey)
from schools_app.models import School


class Communism(models.Model):
    GENDER_CHOICES = (
        ('female', 'female'),
        ('male', 'male'),
        ('-', '-'),
    )

    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='-'
    )
    abstract = True


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    id_school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self, *args):
        for field_name in ['name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Department, self).save(*args)


class Position(models.Model):
    name = models.CharField(max_length=255)

    description = models.TextField()
    is_active = models.BooleanField(default=True)
    permission = models.CharField(max_length=255)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

    def save(self, *args):
        for field_name in ['nane']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Position, self).save(*args)


class Employee(Communism, models.Model):
    duration = models.PositiveIntegerField()
    id_position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['second_name']

    def __str__(self):
        return f'{self.second_name}' f' {self.first_name}'

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'second_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Employee, self).save(*args, **kwargs)
