# Generated by Django 4.0.6 on 2022-07-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communism',
            old_name='phone_number_1',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='communism',
            name='phone_number_2',
        ),
        migrations.RemoveField(
            model_name='communism',
            name='phone_number_3',
        ),
        migrations.RemoveField(
            model_name='communism',
            name='phone_number_4',
        ),
        migrations.RemoveField(
            model_name='communism',
            name='phone_number_5',
        ),
        migrations.AlterField(
            model_name='communism',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='communism',
            name='second_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
