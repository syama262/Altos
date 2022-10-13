# Generated by Django 4.1.1 on 2022-09-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=255)),
                ('emp_email', models.CharField(max_length=255)),
                ('emp_phone', models.CharField(max_length=255)),
                ('emp_designation', models.CharField(max_length=255)),
                ('emp_salary', models.IntegerField()),
            ],
        ),
    ]
