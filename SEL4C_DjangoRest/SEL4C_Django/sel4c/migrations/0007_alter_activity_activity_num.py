# Generated by Django 4.2.4 on 2023-10-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sel4c', '0006_alter_activity_activity_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_num',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)], unique=True),
        ),
    ]