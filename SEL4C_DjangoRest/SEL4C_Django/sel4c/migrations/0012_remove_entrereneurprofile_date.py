# Generated by Django 4.2.6 on 2023-10-20 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sel4c', '0011_entrereneurprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entrereneurprofile',
            name='date',
        ),
    ]