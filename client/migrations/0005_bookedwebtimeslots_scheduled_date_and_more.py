# Generated by Django 4.0.2 on 2022-02-03 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_bookedwebtimeslots'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedwebtimeslots',
            name='scheduled_Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='bookedwebtimeslots',
            name='scheduled_Time',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='bookedwebtimeslots',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]