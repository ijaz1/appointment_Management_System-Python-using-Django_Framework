# Generated by Django 4.0.2 on 2022-02-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=50)),
                ('last_Name', models.CharField(max_length=50)),
                ('phone_Number', models.BigIntegerField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
