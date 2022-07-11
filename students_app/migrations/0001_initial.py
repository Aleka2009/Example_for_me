# Generated by Django 4.0.6 on 2022-07-11 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees_app', '0001_initial'),
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('communism_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='employees_app.communism')),
                ('id_course', models.ManyToManyField(to='courses_app.course')),
            ],
            options={
                'ordering': ['second_name'],
            },
            bases=('employees_app.communism', models.Model),
        ),
    ]
