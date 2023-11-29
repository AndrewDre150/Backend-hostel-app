# Generated by Django 4.2.7 on 2023-11-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=120)),
                ('phone_number', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('course', models.CharField(max_length=120)),
                ('college_name', models.CharField(max_length=120)),
                ('full_name', models.CharField(max_length=120)),
                ('emergency_contact', models.CharField(max_length=20)),
                ('confirmation', models.BooleanField(default=False, verbose_name='I confirm the information provided')),
            ],
        ),
    ]