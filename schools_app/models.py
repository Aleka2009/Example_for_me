from django.db import models

# school_class:
# 			name
# 			location
# 			contacts


class School(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args):
        for field_name in ['name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(School, self).save(*args)

