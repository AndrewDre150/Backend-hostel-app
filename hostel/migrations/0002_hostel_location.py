# Generated by Django 4.2.7 on 2023-11-06 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostel',
            name='location',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
